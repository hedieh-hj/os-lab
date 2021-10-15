x = int(input("Enter a number: "))  
sum = 0  
temp = x  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if x == sum:  
   print(" ( YES ) ",x,"is an Armstrong number")  
else:  
   print(" ( NO ) ",x,"is not an Armstrong number")  