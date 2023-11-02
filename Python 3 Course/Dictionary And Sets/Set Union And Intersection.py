n = int(input("Enter size of set: "))
s1 = set()
s2 = set()

print("Enter elements in set1\n")
for i in range(n):
    x = int(input(f"s1[{i}] = "))
    s1.add(x)

print("Enter elements in set2\n")
for j in range(n):
    y = int(input(f"s2[{j}] = "))
    s2.add(y)

print(f"Set1: {s1}"); print(f"Set2: {s2}")
print(f"Union of two sets are: {s1.union(s2)}")
print(f"Intersection of two sets are: {s1.intersection(s2)}")
