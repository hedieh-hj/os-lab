
import os
os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
   
#print (color.GREEN + 'test')
x=1
i=1
while x>0:
    
    if i==1:

        x = int(input("enter row: "))
        y = int(input("enter column: "))
        print()
        for i in range(1,x+1):
            for j in range(1,y+1):
                #print(format(i*j,'4d'),end=' ')
                if (int (i)== int (j)):
                    print(color.RED + '{:<4}'.format(i*j), end=' ')
                else:
                    print(color.WHITE+'{:<4}'.format(i*j), end=' ')    
            print("")
        i=int(input(color.WHITE+"\nif you want start it , please insert 1 : "))

    else :
        print("Good Bye !")
        input()
        break

