from os import close
from os import read
from os import write

def show_menu():
    print("""\n  ********* welcome to my store (hediye jamili) *********
    1.add
    2.edit
    3.remove
    4.show list
    5.search
    6.buy
    7.exit""")

def load():

    ff = open('storetxt.txt', 'r')
    line = ff.read().split('\n')
        
    for x in line:
        dict = {}
        if not x:
            break
        x = x.split(',')
        dict['code'] = x[0]
        dict['name'] = x[1]
        dict['price'] = float(x[2])
        dict['count'] = int(x[3])
        all[x[0]] = dict

    ff.close()

def add():

    print('\n*** add new product ***\n')
    code = input('code: ')
    name = input('name: ')
    price = input('price: ')
    count = input('count: ')
    dict = {}
    dict['code'] = code
    dict['name'] = name
    dict['price'] = float(price)
    dict['count'] = int(count)
    all[code] = dict

def edit():
    code = input('You can edit product by their code: ')
    try:
        all[code]

        name  = input('new name : ')
        all[code]['name'] = name

        price = int(input('new price : '))
        all[code]['price'] = price

        count = int(input('new count : '))
        all[code]['count'] = count

        print('\nmission complete ! \n')
    except:
        print('\nyou enter a wrong code ! please try again ... ')

def remove():
    code = input('enter the code of product that you want remove it. : ')
    try:
        del all[code]
        print('\nmission complete!')
    except:
        print('\nyou enter a wrong code ! please try again ...')

def search():
    i=1
    while 1:
        
        if i==1:
            found=0
            name = input('enter name of product which you want : ')

            for key, txt in all.items():
                if txt['name']==name:
                    found = 1
                    break
            if found==1:
                print('We have %s in our store.\n'%name)
            else:
                print('we do not have it.')
            i=int(input('\ndo you want to search another one ? yes=1 no=2 : '))
        else:
            break
                
def buy():
    cost = {}
    i=1
    while 1:
        if i==1:
            code = input('code : ')
            if code in all.keys():
                while 1:
                    x=int(all[code]['count'])
                    c = input('How many : ')
                    if 0 < int(c) <= x:
                        all[code]['count'] -= int(c)
                        cost[code] = {code:code, 'name':all[code]['name'], 'price':float(all[code]['price']), 'count':int(c)}
                        if all[code]['count']==0:
                            del all[code]
                        print('mission complete !')
                        break
                    else:
                        print('it is out of service. we have only %i .' %all[code]['count'])
            else:
                print('you enter a wrong code ! please try again ...')
        
    
            print('\n____________________________\nThis is your bill:\ncode\t\tname\t\tprice\t\tcount')
            totalcost = 0
            for key, y in cost.items():
                print('%s\t\t%s\t\t%f\t%i'%(key, y['name'], y['price'], y['count']))
                totalcost = totalcost + (y['price']*y['count'])
            print('\nYou have to pay %f $ .'%totalcost)
            print('____________________________')
            i=int(input('\ndo you want to buy another one ? yes=1  no=2 : '))
        else:
            break    
def show_list ():
   print('\ncode\t\tname\t\tprice\t\tcount\n')
   for key, x in all.items():
       print('%s\t\t%s\t\t%f\t%i' %(key, x['name'], float(x['price']), int(x['count'])))
   print()

def save():
    ff = open('storetxt.txt', 'w')
    for key, x in all.items():
        ff.write('%s,%s,%s,%s\n' %(key, x['name'], str(x['price']), str(x['count']))) 

def reset():
    #save()
    load()    

while 1: 
    all={}
    #load()
    reset()
    show_menu()
    
    select=int(input("\nplease enter your number : "))

    if select == 1:
        add()
        save()

    if select == 2:
        edit() 
        save()
    if select == 3:
        remove()
        save()
    if select == 4:
        show_list()
        save()
    if select == 5:
        search()    

    if select == 6:
        buy()    
        save()
    if select == 7:
        save()
        exit()    