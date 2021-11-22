from math import gcd 

class Fraction:
    def __init__(self, x=None, y=None): #none mizarim baray tavabe ke avalesh result= Fraction() darim ya 0
        self.x = x   #self.x -> be jay x mishe chiz dg ham gozasht 
        self.y = y
        

    def simplify(self , second):
        simple=gcd(second.x , second.y)
        second.x = second.x  // simple  
        second.y = second.y //  simple
        return second
        

    def sum(self, second):         #self kasr aval mishe chon a.sum(b) mizanim  =def sum(self,first,secon)
        result = Fraction()        #khode result ham bayd az oe fraction bashe 
        result.x = self.x*second.y + self.y*second.x
        result.y = self.y*second.y
        return self.simplify(Fraction(result.x,result.y))


    def sub(self, second):
        result = Fraction()
        result.x = self.x*second.y - self.y*second.x
        result.y = self.y*second.y
        return self.simplify(Fraction(result.x,result.y))

        #rah 2
        # result.x = self.x*second.y - self.y*second.x
        # result.y = self.y*second.y
        # result = Fraction(result.x,result.y)
        # return result
        
        #rah 3
        #return Fraction (self.x*second.y - self.y*second.x  , self.y*second.y)


    def multiple(self, second):
        result = Fraction()    
        result.x = self.x*second.x
        result.y = self.y*second.y
        return self.simplify(Fraction(result.x,result.y))


    def divide(self, second):
        result = Fraction()
        result.x = self.x*second.y
        result.y = self.y*second.x
        return self.simplify(Fraction(result.x,result.y))



    def show(self):
        return str(self.x) + '/' + str(self.y)

xx= list(map(int, input('enter fraction1: e.g. x/y\n').split('/')))
yy= list(map(int, input('enter fraction2: e.g. x/y\n').split('/')))
a = Fraction(xx[0], xx[1])
b = Fraction(yy[0], yy[1])
print('sum: %s\tsub: %s\tmul: %s\tdiv: %s'%((a.sum(b)).show(), (a.sub(b)).show(), (a.multiple(b)).show(), (a.divide(b)).show()))

