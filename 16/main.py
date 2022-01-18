from asyncio.windows_events import NULL
import sqlite3
from functools import partial
import qdarkstyle
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader



class MainWindow(QMainWindow):
    def __init__(self ,ui):
        super().__init__()

        self.db = NULL

        #loader=QUiLoader()
        #self.ui=loader.load("test.ui")
        self.ui=dark
        self.ui.show()


        self.conn = sqlite3.connect("contact.db")
        self.my_cursor = self.conn.cursor()

        self.ui.remove_esp.clicked.connect(partial(self.remove_selected))
        self.ui.remove_all.clicked.connect(partial(self.remove_all))
        self.ui.save.clicked.connect(partial(self.Form))
        self.load_data()


    def load_data(self):  #load all information of database
            self.my_cursor.execute("SELECT * FROM people")
            self.db = self.my_cursor.fetchall()  
            self.update_table()



    def remove_selected(self): #remove especial contact
            selected1 = self.ui.tableWidget.currentRow()
            self.ui.tableWidget.removeRow(selected1)
            self.my_cursor.execute(f"DELETE FROM people WHERE name ='{self.db[selected1][1]}';")
            self.conn.commit()
            self.db.pop(selected1)



    def remove_all(self): #remove all contacts
            self.ui.tableWidget.setRowCount(0)
            self.db = NULL
            self.my_cursor.execute(f"DELETE FROM people;")
            self.conn.commit()          

            

    def Form(self):  # add 
            if self.ui.name_input.text() != '' or self.ui.family_input.text() !=''or self.ui.phone_input.text() !='' or self.ui.mobile_input.text() !=''  or self.ui.email_input.text() !='':
                new_contact = (0,self.ui.name_input.text(),self.ui.family_input.text(),self.ui.phone_input.text(),self.ui.mobile_input.text(),self.ui.email_input.text())
                self.db.append(new_contact)
                self.my_cursor.execute(f"INSERT INTO people (name,family,phone_number,mobile_number,email)VALUES ('{self.ui.name_input.text()}', '{self.ui.family_input.text()}', '{self.ui.phone_input.text()}','{self.ui.mobile_input.text()}','{self.ui.email_input.text()}');")
                self.conn.commit()

                self.update_table()
                self.ui.name_input.setText("")
                self.ui.family_input.setText("")
                self.ui.phone_input.setText("")
                self.ui.mobile_input.setText("")
                self.ui.email_input.setText("")




    def update_table(self):
            self.ui.tableWidget.setColumnCount(5)  
            self.ui.tableWidget.setRowCount(len(self.db))
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tableWidget.setSortingEnabled(True)  
            myListOfHeaderLabels = ['Name' , 'Family' ,'Phone', 'Mobile' , 'Email']
            self.ui.tableWidget.setHorizontalHeaderLabels(myListOfHeaderLabels)       

            for i in range(0,len(self.db)):
                for j in range (1,6):             
                    self.ui.tableWidget.setItem(i,j-1, QTableWidgetItem(self.db[i][j]))      


app = QApplication()
app.setStyleSheet(qdarkstyle.load_stylesheet())

loader=QUiLoader()
dark=loader.load("test.ui")


def mode():
    if dark.darkmode.isChecked():
      app.setStyleSheet(qdarkstyle.load_stylesheet())
    else:
      app.setStyleSheet(None)

dark.darkmode.clicked.connect(partial(mode))

contactlist = MainWindow(dark)


app.exec() #run