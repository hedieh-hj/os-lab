from math import *
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *



class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui', None)
        self.ui.show()

        self.result = 0
        self.lastOperand = ''
        self.step = 0

################################################################################

        self.ui.btn0.clicked.connect(partial(self.func_num, 0))       #tarif kardn adad  push button =btn
        self.ui.btn1.clicked.connect(partial(self.func_num, 1))
        self.ui.btn2.clicked.connect(partial(self.func_num, 2))
        self.ui.btn3.clicked.connect(partial(self.func_num, 3))
        self.ui.btn4.clicked.connect(partial(self.func_num, 4))
        self.ui.btn5.clicked.connect(partial(self.func_num, 5))
        self.ui.btn6.clicked.connect(partial(self.func_num, 6))
        self.ui.btn7.clicked.connect(partial(self.func_num, 7))
        self.ui.btn8.clicked.connect(partial(self.func_num, 8))
        self.ui.btn9.clicked.connect(partial(self.func_num, 9))
        
################################################################################        

        self.ui.sum_btn.clicked.connect(self.sum)       #tarif def - operand
        self.ui.sub_btn.clicked.connect(self.sub)
        self.ui.mul_btn.clicked.connect(self.mul)
        self.ui.division_btn.clicked.connect(self.div)
        self.ui.equal_btn.clicked.connect(self.equal)
        self.ui.ac_btn.clicked.connect(self.ac)
        self.ui.dot_btn.clicked.connect(self.dot_func)
        self.ui.percent_btn.clicked.connect(self.percent_func)
        self.ui.neg_pos_btn.clicked.connect(self.neg_pos)
        self.ui.log_btn.clicked.connect(self.log_func)
        self.ui.sqrt_btn.clicked.connect(self.sqrt_func)
        self.ui.sin_btn.clicked.connect(self.sin_func)
        self.ui.cos_btn.clicked.connect(self.cos_func)
        self.ui.tan_btn.clicked.connect(self.tan_func)
        self.ui.cot_btn.clicked.connect(self.cot_func)

################################################################################

    def func_num(self, num):
        self.ui.textBox.setText(self.ui.textBox.text() + str(num))  #textbox=line edit
    
    
    def dot_func(self):
        if '.' not in self.ui.textBox.text():
            self.ui.textBox.setText(self.ui.textBox.text() + '.')
    
    def sum(self):
        try:
            self.result += float(self.ui.textBox.text())
            self.lastOperand = '+'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    
    def sub(self):
        try:
            if self.step == 0:
                self.result = float(self.ui.textBox.text())
            else:
                self.result -= float(self.ui.textBox.text())
            self.lastOperand = '-'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    
    def mul(self):
        try:
            if self.step == 0:
                self.result = float(self.ui.textBox.text())
            else:
                self.result *= float(self.ui.textBox.text())
            self.lastOperand = '*'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    
    def div(self):
        try:
            if self.step == 0:
                self.result = float(self.ui.textBox.text())
            else:
                self.result /= float(self.ui.textBox.text())
            self.lastOperand = '/'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    
    def equal(self):
        self.last_num = float(self.ui.textBox.text())
        self.step += 1
        if self.lastOperand == '+':
            self.result += self.last_num

        elif self.lastOperand == '-':
            self.result -= self.last_num

        elif self.lastOperand == '*':
            self.result *= self.last_num

        elif self.lastOperand == '/':
            self.result /= self.last_num

        elif self.lastOperand == '%':
            self.result = self.last_num/100
        else:
            self.result = self.last_num

        self.ui.textBox.setText(str(self.result))
        self.result = 0
        self.step = 0
        self.lastOperand = ''
    
    def ac(self):
        self.result = 0
        self.ui.textBox.setText('')
        self.step = 0
        self.lastOperand = ''
    
    def percent_func(self):
        self.ui.textBox.setText(str(float(self.ui.textBox.text())/100))
        self.lastOperand = '%'
        self.step += 1
    
    def neg_pos(self):
        if '-' in self.ui.textBox.text():
            self.ui.textBox.setText(self.ui.textBox.text()[1:])
        else:
            self.ui.textBox.setText('-' + self.ui.textBox.text())


    def sin_func(self):
        self.result=float(self.ui.textBox.text())
        self.result=self.result/360 *2 * pi
        self.result=round(sin(self.result),5)
        self.ui.textBox.setText(str(self.result))
        self.lastOperand = 'sin'
        self.step += 1

    
    def cos_func(self):
        self.result=float(self.ui.textBox.text())
        self.result=self.result/360 *2 * pi
        self.result=round(cos(self.result),5)
        self.ui.textBox.setText(str(self.result))
        self.lastOperand = 'cos'
        self.step += 1
    

    def tan_func(self):
        self.result=float(self.ui.textBox.text())
        self.result=self.result/360 *2 * pi
        self.result=round(tan(self.result),5)
        self.ui.textBox.setText(str(self.result))
        self.lastOperand = 'tan'
        self.step += 1
    

    def cot_func(self):
        self.result=float(self.ui.textBox.text())
        self.result=self.result/360 *2 * pi
        self.result=round(atan(self.result),5)
        self.ui.textBox.setText(str(self.result))
        self.lastOperand = 'cot'
        self.step += 1
    

    def log_func(self):
        self.ui.textBox.setText(str(round(log(float(self.ui.textBox.text()), 10), 4)))
        self.lastOperand = 'log'
        self.step += 1
    

    def sqrt_func(self):
        self.ui.textBox.setText(str(round(sqrt(float(self.ui.textBox.text())), 4)))
        self.lastOperand = 'sqrt'
        self.step += 1
        
################################################################################

#if __name__==" __main__": # ghesmat main
    
app = QApplication([])  #har app chand window dare 
calculatorx=Calculator() # aval bayd shey az qapplication besazi
app.exec()  #run kardn dar while 