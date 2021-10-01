import math
i=1
while True:
    if i==1:
        r=float(input("enter the radius of circle : "))

        area=r*r*(math.pi)
        perimeter=2*(math.pi)*r

        print("area = ", area)
        print("perimeter = ", perimeter)

        i=int(input("if you want to try it again press 1 : "))
    
    else:
        print("Good bye !")
        input()