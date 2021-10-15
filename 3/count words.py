
x=1
i=1
while x>0:
    

    if i==1:
        list=[ word for word in input(" enter your sentece (without . ): ").split( )]
        a=len(list)
        print ("number of words is :  ", a)
        i=int(input("if you want start it , please insert 1 : "))
        

    else :
        print("Good Bye !")
        input("press enter for exit!")
        break
