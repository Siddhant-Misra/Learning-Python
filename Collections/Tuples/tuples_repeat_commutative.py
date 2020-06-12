tuple1 = (1, 3) 
tuple2 = (2, 4)
 
print("The original tuple : " + str(tuple1)) 
print("The original tuple : " + str(tuple2)) 

N = 4

result = ((tuple1, ) * N) 
result2 = ((tuple2, ) * N)

print("The duplicated tuple elements are : " + str(result)) 
print("The duplicated tuple elements are : " + str(result2))
print("--------------")

resultx = result + result2
resulty = result2 + result

print("The tuple elements commutative : " + str(resultx))
print("The tuple elements commutative : " + str(resulty))  



