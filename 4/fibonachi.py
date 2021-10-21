
a=int(input("enter your number : "))
a1=1
a2=1
#print(1 ,",", 1 , end = ' ')

i=1
for i in range(a):
    if i<2 :
        print(1,end=',')

    if i>=2:    
        t=a1
        a1=a2
        a2=a2+t
        if(i==a-1):
            print(a2)
        else:    
            print(a2,end =',')
        i=i+1
input()        