import random
from termcolor import colored 
y=1
while True:
    if y==1:

        list=["rock","paper","scissors"]
        i=0
        count1=0
        count2=0

    
        print("\n\n *******rock 👊  paper 🤚 scissors ✌ *******\n") 

        while i != 5:

                print("\nscore player : ", count1 ,  "\nscore bot  : " , count2 , "\nround : ",i+1 )
                player1=input("\nwrite your choice  (rock 👊  paper 🤚 scissors ✌) = ")

                if player1=="rock" or player1=="paper" or player1=="scissors"  :
                    flag = 1
                    winflag = 1
                    while flag == 1:
                                
                        player2=random.choice(list)
                        print("bot choice (rock 👊  paper 🤚 scissors ✌) = " , player2)
                        flag=0
                        if (player1=="rock" and player2=="scissors" ) or (player1=="paper" and player2=="rock") or (player1=="scissors" and player2=="paper"):
                            count1+=1
                            i+=1
                            if count1==5 :
                                print(colored("\n*** winner = player 1 ***\n", 'green'))
                                winflag = 0
                                break
                            

                        elif (player2=="rock" and player1=="scissors" ) or (player2=="paper" and player1=="rock") or (player2=="scissors" and player1=="paper"):
                            count2+=1
                            i+=1   
                            if count2==5:
                                print(colored("\n*** winner = player 2 ***\n", 'green')) 
                                winflag = 0
                                break   

                        else :
                            i+=1

                    if winflag == 0:
                        break        
                        

                else:
                    print(colored ("\nyou write a illegal word player 1 ! try again...\n" , 'red') )


        if i==5:
        
        
            if (count1 > count2 ):
                print("\nscore player : ", count1 ,  "\nscore bot  : " , count2 )
                print(colored("\n*** winner = player ***\n", 'green'))
            
            if (count1 < count2 ):
                print("\nscore player : ", count1 ,  "\nscore bot  : " , count2 )
                print(colored("\n*** winner = bot ***\n", 'green'))  
            
            if (count1 == count2 ):
                print("\nscore player : ", count1 ,  "\nscore bot  : " , count2 )
                print(colored("\n*** winner = player & bot ***\n", 'green'))  

        y=int(input (" do you want to play it again ? yes=1  no=2 : "))

    else :
        print("Good bye !")
        input()
        break            
                   
            

   