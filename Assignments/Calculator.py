"""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit

But with infinite choices. 
"""

"""
1. Get the digits as a string
2. Spilt the string with spaces
3. Write a for loop that will convert the strings to integers in said list
4. Then sum of function for addition etc
"""
print("Welcome to Calculator!")

class Calculator:
    def addition(self,x,y):
        added = x + y
        return added
    def subtraction(self,x,y):
        subtracted = x - y
        return subtracted
    def multiplication(self,x,y):
        multiplied = x * y
        return multiplied
    def division(self,x,y):
        divided = x / y
        return divided

calculator = Calculator()

print("1 \tAddition")
print("2 \tSubtraction")
print("3 \tMultiplication")
print("4 \tDivision")
operations = int(input("What operation would you like to use?:  "))

x = int(input("How many numbers would you like to use?:  "))

if operations == 1:
    a = 0
    sum = 0
    while a < x:
        number = int(input("Please enter number here:  "))
        a += 1
        sum = calculator.addition(number,sum)
    print("The answer is", sum)
if operations == 2:
    s = 0
    diff = 0
    while s < x:
        number = int(input("Please enter number here:  "))
        s += 1
        diff = calculator.subtraction(number,diff)
    print("The answer is", diff)
if operations == 3:
    m = 0
    prod = 1
    while m < x:
        number = int(input("Please enter number here:  "))
        m += 1
        prod = calculator.multiplication(number, prod)
    print("The answer is", prod)
if operations == 4:
    d = 0
    quo = 1
    while d < x:
        number = int(input("Please enter number here:  "))
        d += 1
        quo = calculator.division(number, quo)
    print("The answer is", quo)