#calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x//y
def rem(x,y):
    return x%y
def pow(x,y):
    return x**y

x=float(input("Enter 1st number:"))
y=float(input("Enter 2nd number:"))
o=str(input("operation:"))

if o.lower()=="add":
    r=add(x,y)
    print(r)
elif o.lower()=="sub":
    r=sub(x,y)
    print(r)
elif o.lower()=="mul":
    r=mul(x,y)
    print(r)
elif o.lower()=="div":
    r=div(x,y)
    print(r)
elif o.lower()=="rem":
    r=rem(x,y)
    print(r)
elif o.lower()=="pow":
    r=pow(x,y)
    print(r)