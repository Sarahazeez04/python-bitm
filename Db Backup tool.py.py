import shutil
import os
import datetime
import time

def create_record(filename, record):
    try:
        with open(filename, 'a') as file:
            file.write(','.join(record) + '\n')
        print("Record created successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def read_records(filename):
    try:
        with open(filename, 'r') as file:
            records = [line.strip().split(',') for line in file]
  
        print("Records:")
        for record in records:
            print(record)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def update_record(filename, old_record, new_record):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        updated_lines = [','.join(new_record) + '\n' if old_record in line else line for line in lines]
        with open(filename, 'w') as file:
            file.writelines(updated_lines)
        print("Record updated successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def delete_record(filename, record):
    try:
        # Convert record to string
        record_str = ','.join(record)

        with open(filename, 'r') as file:
            lines = file.readlines()
        updated_lines = [line for line in lines if record_str not in line]
        with open(filename, 'w') as file:
            file.writelines(updated_lines)
        print("Record deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def backup_file(source_file, backup_directory, backup_time):
    try:
        # Create backup directory if it doesn't exist
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        # Get the filename and extension
        file_name, file_extension = os.path.splitext(source_file)

        # Generate timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Construct new filename with timestamp
        backup_file_name = f"{file_name}_{timestamp}{file_extension}"

        # Backup the file
        backup_file_path = os.path.join(backup_directory, backup_file_name)

        # Calculate the time until the backup
        current_time = datetime.datetime.now().strftime("%H:%M")
        time_difference = (datetime.datetime.strptime(backup_time, "%H:%M") - datetime.datetime.strptime(current_time, "%H:%M")).total_seconds()

        # Wait until the backup time
        time.sleep(time_difference)

        shutil.copy2(source_file, backup_file_path)
        print(f"File backed up to: {backup_file_path}")
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")

def restore_backup(backup_file_path, target_file):
    try:
        shutil.copy2(backup_file_path, target_file)
        print(f"Backup file '{backup_file_path}' restored successfully.")
    except FileNotFoundError:
        print(f"Error: Backup file '{backup_file_path}' not found.")

def monitor_backups(backup_directory):
    while True:
        # List all files in the backup directory
        files = os.listdir(backup_directory)
        if len(files) == 0:
            print("Backup Pending...")
        else:
            print("\nBackup Status:")
            for file in files:
                print(f"Backup file: {file}")
            print("Backup Completed")
        time.sleep(5)  # Check every minute
        return


def menu():
    print("\nMenu:")
    print("1. Create Record")
    print("2. Read Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Backup File")
    print("6. Restore Backup")
    print("7. Monitor Backup Status")
    print("8. Exit")

if __name__ == "__main__":
    backup_directory = "backup"
    filename = "file.txt"

    # Ensure the backup directory exists
    os.makedirs(backup_directory, exist_ok=True)

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            record = input("Enter record (id,name,data): ").split(',')
            create_record(filename, record)
        elif choice == "2":
            read_records(filename)
        elif choice == "3":
            old_record = input("Enter record ID to update: ")
            new_record = input("Enter new record (id,name,data): ").split(',')
            update_record(filename, old_record, new_record)
        elif choice == "4":
            record = input("Enter record (id,name,data) to delete: ").split(',')
            delete_record(filename, record)
        elif choice == "5":
            backup_time = input("Enter backup time (HH:MM): ")
            backup_file(filename, backup_directory, backup_time)
        elif choice == "6":
            backup_file_name = input("Enter the backup file name to restore: ")
            backup_file_path = os.path.join(backup_directory, backup_file_name)
            restore_backup(backup_file_path, filename)
        elif choice == "7":
            monitor_backups(backup_directory)
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
