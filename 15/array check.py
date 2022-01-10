
t=1
while True:
    if t==1 : 
        array = input("enter your array e.g. 1,2,3 (with , between number): ")
        arraylist = array.split(",")
        length = len(arraylist)
        test = 0

        for i in range(length):

            if arraylist[i] ==  arraylist[length - 1]:
                test = 1

            else :
                test = 0
                break

            length -= 1


        if test == 0:
            print("this array is not  symmetrical.")
        if test == 1:
            print("this array is symmetrical.")

        t=int(input("\ndo you want try again ? yes = press 1   ,   no = press 2  : "))

        if t==2:
            print("Good Bye!")
            exit()    