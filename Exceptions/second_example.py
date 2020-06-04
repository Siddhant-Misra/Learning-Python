try: 
    print('In try block')
    10 /0 
    10 /10 
except Exception as ex:
    print('In except block') 
    print(f'\t{ex =}')
else: 
    print('No error. So, in else block')
finally: 
    print('In finally block')

print('next statement')