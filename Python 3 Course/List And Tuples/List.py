# Lists:- Mutable Data Type. Change, modified or delete the elements.
list1 = [12,7,1,6,1,5,7,23]

# List Slicing
print(list1[0:6])
print(list1[::-1])
print(list1[1:6])
print(list1[0::3])
print(list1[-1:])

# List Methods
list1.reverse(); print(list1)
list1.pop(2); print(list1)
list1.remove(5); print(list1)
list1.append(56); print(list1)
list1.insert(5,575); print(list1)

# Tuples:-  Immutable data type. Can't change,modified or delete the elements.

t1 = (1,2,4,2,4,77)
print(t1.count(4))
print(t1.index(2))

