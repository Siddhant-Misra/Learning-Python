"""
Purpose: working withs Lists

    Properties of Lists
        - List is representing using [].
        - It can store asymmetric data types
        - List can be classified as single-­dimensional and multi­-dimensional.
        - Lists will retain the properties of elements stored within them.
        - Lists is a mutable object, which means elements in list can be changed.

"""
# Homogenous list
numbers = [12, 334, 23, 2, -323]
print('numbers     =', numbers)
print('type(numbers)', type(numbers))

# non-homogenous
numbers = [12, 3.4, -0.00004, None, 'abc', True, 4 + 55 / 6]
print('numbers=     ', numbers)
print('type(numbers)', type(numbers))

numbers = [[12, 3.4], (-0.00004, None), {'abc', True, 4 + 55 / 6}]
print('numbers=     ', numbers)
print('type(numbers)', type(numbers))


# multi-dimensional lists
ml = [1, 2, 3, 4.3, 5, [6, 7, 8, (9, 10)]]
#     0  1  2   3   4  --------5--------
#                       0  1  2   --3--
#                                 0   1

print('ml          ', ml)
print('type(ml)    ', type(ml))

print('len(ml)=    ', len(ml))

# Indexing
print('ml[3]        ', ml[3])
print('type(ml[3])  ', type(ml[3]))
# print( ml[6]) # IndexError: list index out of range

print('ml[5]        ', ml[5])

print('ml[5][1]     ', ml[5][1])
print('ml[5][3]     ', ml[5][3])

print('ml[5][3][0]  ', ml[5][3][0])
# ml is a 3-dimensional list


# forward vs reverse indexing
# [1, 2, 3, 4.3, 5, [6, 7, 8, (9, 10)]]
#  0  1  2   3   4   --------5--------  - forward indexing
# -6 -5  -4  -3  -2  ------- -1 ------  - reverse indexing
print('ml[-5]       ', ml[-5])

print(ml[-5] == ml[1])
assert ml[-5] == ml[1]
assert ml[-1] == ml[5]

# Slicing - last value in boundary will not be included
print('ml[1:4]      ', ml[1:4])
print('ml[1:4:2]    ', ml[1:4:2])
print('ml[:4:2]     ', ml[:4:2])
print('ml[::2]      ', ml[::2])
print('ml[::]       ', ml[::])