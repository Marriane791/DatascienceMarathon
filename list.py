#They are  odered changable and allow duplicates and items can be of diffrent data types
fruits = ["Apple","Orange","Mellon","Cherry", "Banana","Kiwi"]
print(fruits[2:])
print(fruits[-1])
#changing an item
fruits[1] = "Blackcurrant"
print (fruits)
print(len(fruits))
fruits.insert(3, "orange")
print(fruits)
groceries = fruits.copy() 
print("these are my groceries:")
print(groceries) 
#you can also instantiate fruits
groceries = list(fruits)
print(groceries)
#you can join two lists using append method
for x in groceries:
    fruits.append(x)
    print(fruits)