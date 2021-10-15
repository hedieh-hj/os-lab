
def BMM(a,b):

    cc = 1
    if a > b:
        x = b
    else:
        x = a
    for i in range(x, 1, -1):
        if ((a % i == 0) and (b % i == 0)):
            cc = i
            break

    print("BMM = " , cc)

 
def KMM (a,b):

    cc = a * b
    if a < b:
        x = b
    else:
        x = a
    for i in range(x, a*b, x):
        if ((i % a == 0) and (i % b == 0)):
            cc = i
            break
    print("KMM = " , cc)

i=1
while True:
    i=int(input("\nenter your choice : \n1.BMM \n2.KMM \n"))
    if i==1 :
     
        x= int(input("enter x :"))
        y= int(input("enter y :"))
        BMM(x, y)  

    if i==2:
        x= int(input("enter x :"))
        y= int(input("enter y :"))
        KMM(x, y)        
        
    i=int(input("do you wanna try again ? press 1 : "))

    if i != 1:
        print("Good bye !")
        input()
        exit


