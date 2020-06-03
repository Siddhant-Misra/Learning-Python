a = input('Enter a binary number : ')   #to get the number
ar = [int(i) for  i in a]
ar  = ar[::-1]                          #reverse the string
res = []                                #empty list
for i in range(len(ar)):                
    res.append(ar[i]*(2**i))
sum_res = sum(res)                      #add the 1's 
print('Decimal Number is : ',sum_res)
