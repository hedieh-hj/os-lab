import math

i=1
while i>0:
    print("\n*** calculator ****")
    print("""
    1.sum
    2.sub
    3.multiplication
    4.division
    5.radikal
    6.sinus
    7.cosine
    8.tangent
    9.cotangent
    10.log
    11.exit
    """)
    text=input("what do you want to do insert number :")

    if int(text)==1:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) + int (b)
        print("sum = ", c)
        

    if int(text)==2:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) - int (b)
        print("sub = ", c)
        

    if int(text)==3:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) * int (b)
        print("multiplication = ", c) 
        

    if int(text)==4:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) / int (b)
        print("division = ", c) 
        

    if int(text)==5:
        a=input("number : ")
        c=int (a)**(1/2)
        print("radical = ", c) 
        


    if int(text)==6:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.sin (math.radians)
        print("sinus = ", float(c))
        

    if int(text)==7:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.cos (math.radians)
        print("cosine = ", float(c))   
        

    if int(text)==8:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.tan (math.radians)
        print("tangent = ", float(c))
        

    if int(text)==9:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.atan (math.radians)
        print("cotangent = ", float(c))
        


    if int(text)==10:
        a=int(input("number : "))
        c=math.log(a)
        print("log = ", c)  
        

    if int(text)==11:
        break