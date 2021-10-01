i=1
while True:
    
    if i==1:
        size=input("enter size of any side of triangle (format: a,b,c): ")

        a,b,c=size.split(",")

        if int(a) + int(b) > int(c) :
            if int(a) + int(c) > int(b):
                if int(c) +int(b) > int(a):
                    print("it can be a triangle!")
                else:
                    print("it can't be a triangle!") 
            else:
                print("it can't be a triangle!")         

        else :
            print("it can't be a triangle!")
        i=int(input("for try it again please insert 1 : "))   

    if i !=1:
        print("Good bye !")
	    
        break        