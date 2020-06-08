
numbers = [88, 99, 666]
print('type(numbers)    =', type(numbers))
print('dir(numbers)     =', dir(numbers))

print("---------")

print("len(numbers)            =", len(numbers))
print("numbers.__len__()       =", numbers.__len__())
assert len(numbers) == numbers.__len__()

print("---------")

print("str(numbers)           =", str(numbers))
print("type(str(numbers))     =", type(str(numbers)))
print("numbers.__str__()      =", numbers.__str__())
print("type(numbers.__str__())=", type(numbers.__str__()))
assert str(numbers) == numbers.__str__()

print("---------")

# List repetition operation - original object not modified
print("numbers * 3         =", numbers * 3)
print('numbers             =', numbers)
print("numbers.__mul__(3)  =", numbers.__mul__(3))
print('numbers             =', numbers)

print("---------")

# List repetition operation - original object IS modified
print("numbers.__imul__(3) =", numbers.__imul__(3))
print('numbers             =', numbers)

print("---------")

print("\nid(numbers)          =", id(numbers))
# object overwriting
numbers = [88, 99, 666]
print("id(numbers)          =", id(numbers))
numbers = [88, 99, 666]
print("id(numbers)          =", id(numbers))
numbers = [88, 99, 666]
print("id(numbers)          =", id(numbers))

print("---------")

# list concatenation
print('numbers\t\t\t=', numbers)
alphabets = ['b', 'c']

print("---------")

print("numbers + alphabets\t=", numbers + alphabets)
print('numbers\t\t\t=', numbers)
print("numbers.__add__(alphabets)=", numbers.__add__(alphabets))
print('numbers\t\t\t=', numbers)

print("---------")

# NOTE: list concatenation will create new object;
# original objects are not changed

print("numbers.__iadd__(alphabets)=", numbers.__iadd__(alphabets))
print('numbers\t\t\t=', numbers)  # first object IS changed

print("---------")

print("numbers.__contains__(12)  =", numbers.__contains__(12))
print("12 in numbers             =", 12 in numbers)

print("---------")

print("numbers.__contains__('b') =", numbers.__contains__('b'))
print("'b' in numbers            =", 'b' in numbers)

print("---------")

print()
print(f'{numbers.__sizeof__()    =}') # object-level size
import sys
print(f'{sys.getsizeof(numbers)  =}') # object + c-header size

print()
print("help(numbers)    =", help(numbers))
print("numbers.__doc__=", numbers.__doc__)
