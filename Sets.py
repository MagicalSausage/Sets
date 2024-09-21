numbers = {1,3,4,5,6,2,5,3}
print(numbers)
#print(numbers[5])
numbers.add(9)
print(numbers)
numbers.remove(2)
print(numbers)
fruits = {"apple","banana","pear"}
food = {"steak","chicken","apple","pear"}
print(fruits.union(food))
print(fruits.intersection(food))
print(fruits.difference(food))
print(food.difference(fruits))
print(food.symmetric_difference(fruits))
fruits2 = {"apple","pear"}
print(fruits.issubset(fruits2))
print(fruits.issuperset(fruits2))