def add():
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    c=a+b
    print(c)

def sub():
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    c=a-b
    print(c)

def prod():
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    c=a*b
    print(c)

def quo():
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    c=a/b
    print(c)

def mod():
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    c=a%b
    print(c)
    
key=int(input("enter key:"))
match(key):
  case 1:add()
  case 2:sub()
  case 3:prod()
  case 4:quo()
  case 5:mod()
  case _:print("invalid")
