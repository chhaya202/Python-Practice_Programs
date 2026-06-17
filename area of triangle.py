# Calculate the area using Heron's formula
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a + b + c) / 2
area =(s * (s - a) * (s - b) * (s - c)) ** 0.5
print(area) 
if(a + b > c and a + c > b and b + c > a):
     print("The area of the triangle is",area)
else:
    print("The given sides do not form a valid triangle.")    