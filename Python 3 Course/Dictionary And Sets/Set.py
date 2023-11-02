# Set is a collection of non repetitive elements or data.
n = int(input("Enter size of given set: "))
s = set()
for i in range(n):
    x = int(input(f"set[{i}] = "))
    s.add(x)
print(f"Given set is: {s}")

# We can't add list or dictionary in set. But tuples are valid in set
s1 = set()
s1.add((1,2,3))
s1.add([1,2,3,4]) # Invalid
s1.add({4:3}) # Invalid
print(s1)