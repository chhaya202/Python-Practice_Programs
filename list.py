# lists functions[unchangable,ordered,indexed]
 
# by loops
number=[]
for i in range(1,11):
    number.append(i)
print(number)
print(len(number))
print(type(number))

# append(add item in end)
number.append(45)
print("append=",number)

#insert(add at specific place)
number.insert(11,40)
print("insert=", number)

#remove(remove given element)
number.remove(40)
print("removed=",number)

#pop(delete element which is at end)
number.pop()
print("pop=",number)