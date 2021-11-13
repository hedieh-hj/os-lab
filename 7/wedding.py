import random  
from colorama import Fore
import pyfiglet

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'elii', 'goli', 'mary', 'mina']

x=int(len(boys))
y=int(len(girls))

randomb = []
randomg = []
result=[]

while len(randomb) != x or len(randomg) != y:

    choose_b = random.randint(0, x-1)
    if boys[choose_b] not in randomb:
        randomb.append(boys[choose_b])
        
    choose_g = random.randint(0, y-1)
    if girls[choose_g] not in randomg:
        randomg.append(girls[choose_g])



result = pyfiglet.figlet_format(" wedding ")
print(result)
print('\nAre you ready to see their chance ?! 💏👀\n')

for i in range (0,x):
    print(Fore.RED + randomg[i],Fore.LIGHTYELLOW_EX + '👰  💍  🤵',Fore.GREEN +   randomb[i], Fore.LIGHTYELLOW_EX +  '    get married :)' ,Fore.WHITE)

print('\nresult=[',end='')
for i in range (0,x):
    print('(',randomg[i],',',randomb[i],')',end='')
print(']')   
print('\n')    

