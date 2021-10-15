import random

array=[]
i=0
while i<=10:
    x=random.randint(0,100)
    if x not in array:
        array.append(x)
        i+=1
print(array)    