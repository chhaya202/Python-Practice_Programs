# simple intrest calculate
Principle=int(input("The value of principle:"))
rate=int(input("The value of rate:"))
time=int(input("The value of time:"))
simpleintrest=(Principle*rate)/time
if(Principle>2000):
 print("The si of:",simpleintrest)
else:
 print("principle is less than 2000")