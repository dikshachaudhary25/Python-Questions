#list operations
list = [1,2,3,4,5]
list.append(6)
list.remove(3)
print("list after all operations: ", list)
print("element at index 2 = ",list[2])

#tuple operations
tuple = (1,2,3,4,5)
tuple1 = (8,9,10)
print("Element at index 3 = ",tuple[3])
print("Slicing tuple = ",tuple[2:4])
print("Concatinating tuple = ",tuple+tuple1)
print("Tuple length = ",len(tuple))

#set operations
set = {1,2,3,4,5}
set1 = {10,9,3,5}
print("union of sets :",set.union(set1))
print("intersection of sets :",set.intersection(set1))
print("difference of sets :",set.difference(set1))
