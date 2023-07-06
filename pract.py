set1={1,2,3,4,5}
set2={3,4,5,6,7}
print("Set1:", set1)
print("Set2:", set2)
print("----------------------------------")
print()
print(set1|set2) #Union of a set
print("The union:", set1.union(set2))
print()
print(set1&set2)#Intersection of a set
print("The intersection:", set1.intersection(set2))
print()
print(set1.difference(set2))
print("Set difference:", set1-set2)
print()
print(set1.symmetric_difference(set2))
print("Symmetric differnce:", set1^set2)
