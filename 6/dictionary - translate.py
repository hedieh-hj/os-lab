from os import read
from os import write
import pyfiglet

def read():
    if x==1:
        #with open("translate.txt", "r") as ff        *mesl khat badishe 
        ff = open("translate.txt", "r")
        num = ff.read().split("\n")
        a=len(num)
        
        for i in range(a):
            
            if i%2 == 0:  # start i=0
                dic={}
                dic["eng"]=num[i]

            if i%2 != 0:
                dic["per"]=num[i]
                temp.append(dic)

        ff.close()
        
    else:
        print("We can\'t found translate.txt file !! ")


#ff=open ("translate.txt","r")
#print(ff.read())
x=1
i=1

while(1):

    temp=[]
    read()


    if i==1:
        result = pyfiglet.figlet_format(" t r a n s l a t e ")
        print(result)
        choose=int(input("enter the number of your choice ?\n\n1.persian to english \n2.english to persian \n3.add word\n4.exit\ninsert : "))

        if choose==1 :
            
            #read()
            org="per"
            tra="eng"
            
            list1=input("\nenter your sentece : ").split( )
            list2=[]
            
            
            for i in list1:
                text=i
                for y in range (len(temp)):
                    if temp[y][org]==i:
                        text = temp[y][tra]
                        #print("testttt : ",text)
                        break
                         
                list2.append(text)

            print("\ntranslate :" , end=" ")
            for name in list2:
                print(name , end=" ")

            

            i=int(input("\n\nif you want start it again , please insert 1 : "))


###################################################################

        if choose==2 :
        
            #read()
            org="eng"
            tra="per"
            
            list1=input("\nenter your sentece : ").split( )
            list2=[]
            
            
            for i in list1:
                text=i
                for y in range (len(temp)):
                    if temp[y][org]==i:
                        text = temp[y][tra]
                        #print("testttt : ",text)
                        break
                         
                list2.append(text)

            print("\ntranslate :" , end=" ")
            for name in list2:
                print(name , end=" ")

            
            i=int(input("\n\nif you want start it again , please insert 1 : "))


###########################################################################
        if choose==3:

            flag=0
            org="eng"
            tra="per"

            ff = open("translate.txt", "a")
            english = input("\neng: ")
            
            for y in range (len(temp)):
                if temp[y][org]==english:
                    text = temp[y][tra]
                    flag=1
                    break
            
            if flag==1 :         
                print("this word exist in the list now :) ")
                print("meaning :" , text)

            else: 
                persian = input("per: ")   
                ff.write("\n"+ english + "\n"+ persian)
                ff.close()
                temp.append({"english":english, "persian":persian})
                print("mission complete!")
    
            i=int(input("\nif you want start it again , please insert 1 : "))

##########################################################################
        if choose==4 :
            print("Good Bye !")
            input("press enter for exit!")
            break