a = [1,2,3,4]
b = ['A']
c = "c"

print a.append(b), a    # None [1, 2, 3, 4, ['A']]
print a.extend(b), a    # None [1, 2, 3, 4, ['A'], 'A']
print a.append(c), a    # None [1, 2, 3, 4, ['A'], 'A', 'c']
print a.extend(c), a    # None [1, 2, 3, 4, ['A'], 'A', 'c', 'c']
