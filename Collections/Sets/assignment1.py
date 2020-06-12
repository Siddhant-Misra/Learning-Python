# try adding a string to both set.add & set.update & observe the difference

a = set()

a.add(1)
a.add(2)

a.update([3,4])

print(a)
# {1, 2, 3, 4}

a.add((5, 6))

print(a)
# {1, 2, 3, 4, (5, 6)}