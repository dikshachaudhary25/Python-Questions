#lambda functions with filter()
my_list = [2, 15, 7, 12, 5, 8, 18]
filtered_list = list(filter (lambda x: x < 10, my_ list))
print(filtered_list)

#lambda functions with map()
x=lambda a,b:a * b
print (x(5,6) )
y=lambda a,b:a + b
print (y (2,3))
z=lambda a,b :a - b print (z (4,3))
a=lambda a,b :a / b print (a (5,8))

#Lambda functions with sorted()
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)
