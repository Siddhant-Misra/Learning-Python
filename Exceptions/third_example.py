try: 
    num1 = int(input('Enter an integer:'))
    num2 = int(input('Enter an integer:'))
except Exception as ex:
    print(f'{ex =}')
    print('-----Please enter integers only----')
else:
    addition = num1 + num2 
    print(f'{addition = }')
finally:
    print('okay this works.')