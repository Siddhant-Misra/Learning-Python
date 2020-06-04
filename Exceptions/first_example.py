try:
    name = 1232
    name.upper()            
    
except Exception as ex:
    print('ex      :', ex)
    print('str(ex) :', str(ex))
    
    print('repr(ex):', repr(ex))
    print(f'{ex = }')


print('\nnext statement')

'''
    # 10 // 0               # ZeroDivisionError
    # 10 / 0                # ZeroDivisionError
    # 10 % 0                # ZeroDivisionError        
    # 10 + '0'              # TypeError
    # 10 + None             # TypeError
    # int('3.1415')         # ValueError
'''