x=1
i=1
while x>0:
    
    if i==1:
        list=[int (x)for x in input ("enter your number with space and when finish press enter : ").split()]
        print("your numbers :  ",list)
        a=int (len(list))
        i=1
        flag=0

        while i < a:
            if(list[i] <= list[i - 1]):
                flag = 1
            i += 1
            

        if (flag==0) :
            print ("Yes, List is sorted.")
        else :
            print ("No, List is not sorted.")
        i=int(input("if you want start it , please insert 1 : "))

    else :
        print("Good Bye !")
        break
