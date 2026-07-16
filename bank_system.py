balance=50000
print("your bank balance is:",balance)
print("1 for deposit")
print("2 for withdarw")

choose=int(input("you want deposit or withdraw:"))
if choose==1:
    deposit=int(input("eneter the amount:"))
    new_balance=balance+deposit
    print("new balance is:",new_balance)
if choose==2:
    withdraw=int(input("eneter the amount:"))
    if withdraw<=balance:
         remaining_balance=balance-withdraw    
         print("Remaining balance is:",remaining_balance)
    else:
        print("insufficent amount")     


