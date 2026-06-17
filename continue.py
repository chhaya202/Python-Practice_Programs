# code for sum of positive number
sum=0
for i in range(10):
    n=int(input("enter the value of n:"))
    if n<0:
       continue
    sum +=n
print(f"sum of positive numbers is: {sum}",)    
    