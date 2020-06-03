"""
Purpose: range() function
    - built-in function
    - Used for sequence generation
    - SYNTAX
        range(INITIAL_VALUE, FINAL_VALUE, STEP)
    - FINAL_VALUE is mandatory
"""

values = range(9)            
print(type(values), values)  

values = range(0, 9)         
print(type(values), values)  

values = range(0, 9, 1)     
print(type(values), values)  


values2 = range(0, 9, 2)
print(list(values2))  # [0, 2, 4, 6, 8]

values2 = range(0, 9, -1)
print(list(values2))  # []

values2 = range(9, 0, -1)
print(list(values2))  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

values2 = range(9, -1, -1)
print(list(values2))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

values2 = range(9, -1, -3)
print(list(values2))  # [9, 6, 3, 0]

#range() is a built in function

print("-------------------------------------")

list(range(0))                     # [] -> range(0, 0, 1)
list(range(1, 0))                  # [] -> range(1, 0, 1)
list(range(1, 0, -1))              # [1]

r = range(0, 20, 2)
print(r)                           

r.count(11)                        # 0
r.count(10)                        # 1
r.index(10)                        # 5

# r[5]  # 10
# r[:5] # range(0, 10, 2)
# r[-1] # 18

range(0) == range(2, 1, 3)         # True
range(0, 3, 2) == range(0, 4, 2)   # True