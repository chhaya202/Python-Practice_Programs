
#print patterns
row=int(input("enter the number of rows:"))
# right angle from left
print("This is right angle triangle from left")
for i in range(1,row+1):
    print("*" * i)

# inverted right angle from right
print("This is inverted right triangle")
for i in range(row,0,-1):
    print("&" * i )        

# right angle  from right 
print(" This is right angle triangle from right")
for i in range(1,row+1):
    print(" " *(row-i) + "$" *i)    

# pyramid pattern    
print("pyramid print")
for i in range(1,row+1):
    print(" "*(row-i),end="")
    print("@" *(2*i-1))

# border print
print("border print only")
for i in range(row):
    for j in range(row):
        if i==0 or i==row-1 or j==0 or j== row-1:
           print("#",end=" ")
        else:
            print(" ",end=" ")
    print()            