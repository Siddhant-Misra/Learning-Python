"""
%d - integer
%i - integer

%c - single char
%s - string/char

%f - floating-point
%F - floating-point

%o - octal
%x - hexadecimal lowercase
%X - hexadecimal uppercase

"""
print("------------------------BEGIN OLD STYLE------------------------------")
#integer
print('' % ())
print('My lucky number is %d') 
print('My lucky number is %d' % (12))

print("------------------------------------------------------")

#string
print('My lucky number is %s' % True)
print('My lucky number is %s' % None)
print('My lucky number is %s' % 1)
print('My lucky number is %s' % "python")

print("------------------------------------------------------")

#repr - same as str but adds an extra quote for strings
print('My lucky number is %r' % True)
print('My lucky number is %r' % None)
print('My lucky number is %r' % 1)
print('My lucky number is %r' % "python")

#printing pi values 
print("------------------------------------------------------")
import math

print(math.pi)            # 3.141592653589793
print('%d' % math.pi)     # 3
print('%f' % math.pi)     # 3.141593
print('%9f' % math.pi)    #  3.141593
print('%9.3f' % math.pi)  #     3.142

print("----------------------------END OLD STYLE--------------------------")
print()
print("----------------------------BEGIN NEW STYLE--------------------------")

print('{} and {}'.format('cat', 'mouse'))
print('{} and {}'.format(213, 'mouse'))
print('{} and {}'.format(213.0, True))
print('{} and {}'.format(None, True))

print("------------------------------------------------------")

print("{}".format(1234567890.88))   # 1234567890.88 
print("{:,}".format(1234567890.88)) # 1,234,567,890.88
print("{:_}".format(1234567890.88)) # 1_234_567_890.88

print("------------------------------------------------------")

print('{:<20}'.format('left aligned'))  # 'left aligned        '
print('{:>20}'.format('right aligned')) # '       right aligned'
print('{:^20}'.format('centered'))      # '      centered      '

print("------------------------------------------------------")
print("------------------------------------------------------")


print('Name:{} Age:{} Salary:{}'.format('udhay', 99, 9999.9999))
print('''Name  :{}
         Age   :{}
         Salary:{}'''.format('udhay', 99, 9999.9999))

print('''Name  :{0}
         Age   :{1}
         Salary:{2}'''.format('udhay', 99, 9999.9999))
#                               0      1     2
