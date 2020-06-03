if 12 > 2:
    print('Fine')
else:
    print('Change')


if 12 > 2:
    print('Fine')
elif 12 > 5:
    print('Change')
else:
    print('Final')


i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, '*', j, '=', i * j)
        j += 1
    print()
    i += 1