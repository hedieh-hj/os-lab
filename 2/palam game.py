import random
from termcolor import colored 
y=1
i=1
while True:
        if y==1:

            list=["palm","back"]
            i=0
            count1=0
            count2=0
            count3=0

            print("\n*******  palm polom plish *******") 

            while i<5: 

                print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
                player=input("\nenter palm or back : ")
                bot1=random.choice(list)
                print("bot 1 : ",bot1)
                bot2=random.choice(list)
                print("bot 2 : ",bot2)
                    
                if player=="palm" or player=="back": 
                    i+=1 

                    if (player=="palm" and bot1=="back" and bot2=="back") or (player=="back" and bot1=="palm" and bot2=="palm"):
                        count1+=1
                        

                    elif (player=="palm" and bot1=="back" and bot2=="palm") or (player=="back" and bot1=="palm" and bot2=="back"):
                        count2+=1
                        

                    elif (player=="palm" and bot1=="palm" and bot2=="back") or (player=="back" and bot1=="back" and bot2=="palm"):
                        count3+=1
                        
                        
                else :
                    print(colored("you enter a illegal word ! try again...","red"))
               

        if (count1 > count2 and count1> count3) or (count3 == count2 and count1> count3):
            print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
            print(colored(" *** winner : player *** ", "green") )   

        if (count1 < count2 and count2> count3) or (count1 == count3 and count1< count2):
            print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
            print(colored(" *** winner : bot 1 *** ", "green") )   

        if (count3 > count2 and count1< count3) or (count1 == count2 and count1< count3):
            print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
            print(colored(" *** winner : bot 2  *** ", "green") ) 

        if (count1 == count2 and count1> count3):
            print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
            print(colored(" *** winner : player  and bot 1 *** ", "green") )   

        if (count3 == count2 and count1< count3):
            print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
            print(colored(" *** winner : bot 1 and bot 2 *** ", "green") )

        if (count1 == count3 and count1> count2):
            print("\n--------------\nscore player: ", count1 ,"\nscore bot 1 : ", count2 ,"\nscore bot 2 : ", count3,"\n-------------")
            print(colored(" *** winner : player and bot 3 *** ", "green") )  

             

        y=int(input ("do you want to play it again ? yes=1  no=2 : "))

        if y==2:
            print("good bye !")
            input()
            break