# calculate quadratic eq for ax**2+bx+c=0
import cmath
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
disc=b*b-4*a*c
print("the value of disc is:",disc)
if(disc>0):
    X1=(-b+cmath.sqrt(disc))/2*a
    X2=(-b-cmath.sqrt(disc))/2*a
    print("The equation has two distinct real roots:",X1,X2)
elif(disc==0):
    x=-b / (2*a) 
    print("The equation has one repeated real root:",x)
else:
     X1=(-b+cmath.sqrt(disc))/2*a
     X2=(-b-cmath.sqrt(disc))/2*a
     print("The equation has two complex roots:",X1,X2)  