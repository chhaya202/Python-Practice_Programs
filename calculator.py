# infinite calculator with function
def add(a,b):
    print(f"{a} + {b} = {a+b}")
def sub(a,b):
    print(f"{a} - {b} = {a-b}")
def multi(a,b):
    print(f"{a} * {b} = {a*b}")
def div(a,b):
    print(f"{a} / {b} = {a/b}")
def modulo(a,b):
    print(f"{a} % {b} = {a%b}")
print("operator value means:- op=1(add) || op=2(sub) ||  op=3(multi) ||  op=4(divide) || op=5(modulo) ||  op>5(invalid)")    
#op means operator
while True:
 op=int(input("enter the value for op:"))
 # for skipping input value
 if op>5:
    print("Invalid! Can't Calculate \U0001F62c")
    continue
# input at runtime    
 a=int(input("enter the value for a:"))
 b=int(input("enter the value for b:"))
 # condition for calling function
 if(op==1):
   add(a,b)
 elif(op==2):
   sub(a,b)
 elif(op==3):
    multi(a,b)
 elif(op==4):
    div(a,b)
 elif(op==5):
    div(a,b)
 else:
    break        


