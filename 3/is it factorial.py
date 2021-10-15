def isFactorialFunc(n):
    sum = 1
    i=1
    while sum<=n:
        sum*=i
        i+=1
        if sum==n:
            return True
    return False

number = int(input("enter your number : "))
if isFactorialFunc(number):
    print('Yes')
else:
    print('No')