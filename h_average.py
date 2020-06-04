# result = eval('1')
# print(f'{result = }')

attempt = 0
while attempt < 5:
    attempt += 1
    
    input_val = eval(input('Enter a number: '))
    print(f'{input_val =}')