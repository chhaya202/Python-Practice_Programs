# break statements
answer=1
for i in range(5):
    n=int(input("enter the value:"))
    if n<=0:
        break
    answer*=n
print(f"multiplication of positive numbers:{answer}")    