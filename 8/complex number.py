import re
class complex :

    def __init__(self, real=None, image=None):
        self.x = real
        self.y = image
        


    def sub(self, second):
        result=complex()
        result.x= self.x - second.x
        result.y= self.y - second.y
        return result


    def sum(self, second):
        result=complex()
        result.x= self.x + second.x
        result.y= self.y + second.y
        return result



    def multiple(self, second):
        result=complex()
        result.x= self.x * second.x - self.y * second.y
        result.y= self.x * second.y - self.y * second.x
        return result


    def show(self):
        return str(self.x) +'+('+str(self.y) +')i'

real1=int(input('enter complex num1 --> real : \t'))
image1=int(input('enter complex num1 --> image : \t'))


real2=int(input('\nenter complex num2 --> real : \t'))
image2=int(input('enter complex num2 --> image : \t'))

a = complex(real1,image1)
b = complex(real2,image2)

print('\nsum: %s\tsub: %s\tmul: %s'% ( (a.sum(b)).show(), (a.sub(b)).show() , (a.multiple(b)).show() ))