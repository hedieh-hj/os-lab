t=1
while True:
    if t==1 : 
        n = int(input("enter you number : "))
        triangleList = []
        for i in range(n):
            temp = []
            if i == 0:
                temp.append(1)
            else:
                for j in range(i+1):
                    if j==0 or j==i:
                        temp.append(triangleList[i-1][j-1])
                    else:
                        temp.append(triangleList[i-1][j]+triangleList[i-1][j-1])
            triangleList.append(temp)
        for i in range(n):
            for j in range(i+1):
                print(triangleList[i][j], end=' ')
            print()
        
        t=int(input("\ndo you want try again ? yes = press 1   ,   no = press 2  : "))

    if t==2:
        print("Good Bye!")
        exit()