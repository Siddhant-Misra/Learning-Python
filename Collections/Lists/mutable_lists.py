"""
Purpose: Mutability of Lists
    - In object value changes 

    id(<obj>) - results the address location where that <obj> is stored 
"""
print('List is a mutable object =======')
ml = [1, 2, 3, 4.3, 5, [6, 7, 8, (9, 10)]]

print('ml           ', ml)
print('id(ml)       ', id(ml))
print('Before ml[3] ', ml[3])

ml[3] = 3.4

print('After ml[3]  ', ml[3])
print('id(ml)       ', id(ml))
print('ml           ', ml)


print('\nString is a immutable object ===')
name = 'Raj Sekhar'
print(f'name         :{name}')
print(f'name[0:3]    :{name[0:3]}')

# name[0:3] = 'Tej'  # TypeError: 'str' object does not support item assignment

# Overwriting changes are supported by every object
print(f'name         :{name}')
print('id(name)      ', id(name))
name = 'Tej Sekhar'  # overwriting the object
print('id(name)      ', id(name))
print(f'name         :{name}')

print()
name = name.replace('Tej', 'Raj')
print('id(name)      ', id(name))
print(f'name         :{name}')