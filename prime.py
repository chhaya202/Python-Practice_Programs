# check the number is prime or not
def prime_check(n):
    if n<=1:
        return False
    for i in range(2,n+1):
        if(n%i==0):
            return False
        return True
while True:    
 n=int(input("enter the value of n:"))
 if prime_check(n):
    print("Prime Number")
 else:
    print("Not Prime Number")        
