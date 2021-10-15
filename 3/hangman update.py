
import os
import random

print(" do you want play with ready words (enter 1) or your own word (enter 2) : ")
ee=int(input())


if ee==1 :
    list=["lion", "zebra", "rabit","ant","horse","monkey","dunkey","chitah","dog","cat","cow","sheep","elephant"]
    word=random.choice(list)
    a=len(word)
    x = ''
    i = a

    while i > 0:      
        check = 0             
        for char in word:  
            
            if char in x:    
                print (char,end="   ")
                check += 1
                
            else:
                print ("__",end="   ")
            
        print("\n\nYou have (", i , ") times for guess")
                
        if check == a:        
            print ("\n -------- * congratulation You won * ------ \n")
            input ("press enter to exit !\n") 
            break  
                        
        guess = input("guess a character : ")
        print("\n") 
        guess=guess.lower() 
        x += guess                    
        if guess not in  word:  
            i -= 1        
            print("Wrong : ", guess)
            print("\n")      
            if i == 0:           
                print ("\n --------- *sorry You lose * --------")
                input ("press enter to exit !\n")  





if ee== 2 :
    word = input("write your word , please ? : ")
    os.system('cls')
    word=word.lower()
    a=len(word)
    x = ''
    i = a

    while i > 0:      
        check = 0             
        for char in word:  
            
            if char in x:    
                print (char,end="   ")
                check += 1
                
            else:
                print ("__",end="   ")
            
        print("\n\nYou have (", i , ") times for guess")
                
        if check == a:        
            print ("\n -------- * congratulation You won * ------ \n")
            input ("press enter to exit !\n") 
            break  
                        
        guess = input("guess a character : ")
        print("\n") 
        guess=guess.lower() 
        x += guess                    
        if guess not in  word:  
            i -= 1        
            print("Wrong : ", guess)
            print("\n")      
            if i == 0:           
                print ("\n --------- *sorry You lose * --------")
                input ("press enter to exit !\n")  
