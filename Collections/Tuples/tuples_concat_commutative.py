tuple1 = (1, 2, 3) 
tuple2 = (4, 5) 

print("The original tuple 1 : " + str(tuple1)) 
print("The original tuple 2 : " + str(tuple2)) 
  
result = tuple1 + tuple2 
result2 = tuple2 + tuple1
  
print("The tuple after concatenation is : " + str(result)) 
print("------------------")
print("The tuple after concatenation is : " + str(result2)) 
