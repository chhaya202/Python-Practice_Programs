# Input the value of n
n = int(input("Enter a positive integer: "))

# Initialize the sum variable
sum = 0

# Calculate the sum using a for loop
for i in range(1,n+1):
    sum= i+sum

# Display the result
print("The sum of the first",n,"natural numbers is",sum)
