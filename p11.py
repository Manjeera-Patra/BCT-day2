#calculator
x=float(input("Enter 1st number:"))
y=float(input("Enter 2nd number:"))
o=str(input("operation:"))
if(o=="+"):
    def add(x,y):
        return x+y
    print(add(x,y))
elif(o=="-"):
    def sub(x,y):
        return x-y
    print(sub(x,y))
elif(o=="*"):
    def mul(x,y):
        return x*y
    print(mul(x,y))
elif(o=="//"):
    def div(x,y):
        return x//y
    print(div(x,y))