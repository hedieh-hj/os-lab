
def table (x,y):
    for i in range(1,x+1):
            for j in range(1,y+1):
                if (i%2 != 0 ):
                    if(j%2 == 0):
                        print("*", end=' ')
                    else:
                        print("#", end=' ')    
                if(i%2 == 0):
                    if(j%2 != 0):
                        print("*", end=' ')
                    else:    
                        print("#", end=' ')    
            print("")


i=1
x=1
while x>0:
    
    if i==1:

        x = int(input("enter row: "))
        y = int(input("enter column: "))
        table(x,y)
        i=int(input("if you want start it , please insert 1 : "))
    else :
        print("Good Bye !")
        input()
        break