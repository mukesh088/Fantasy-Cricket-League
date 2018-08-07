# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalmn.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from Evaluate import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 601, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.edit1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit1.setObjectName("edit1")
        self.horizontalLayout_8.addWidget(self.edit1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.edit2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit2.setObjectName("edit2")
        self.horizontalLayout_8.addWidget(self.edit2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.edit3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit3.setObjectName("edit3")
        self.horizontalLayout_8.addWidget(self.edit3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.edit4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit4.setObjectName("edit4")
        self.horizontalLayout_8.addWidget(self.edit4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 260, 601, 281))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_9.addWidget(self.listWidget_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_9.addWidget(self.listWidget)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 180, 601, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_11.addWidget(self.lineEdit_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_11.addWidget(self.lineEdit_5)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 220, 261, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_12.addWidget(self.radioButton_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_12.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_12.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_12.addWidget(self.radioButton)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(350, 220, 261, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_13.addWidget(self.lineEdit_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        
        self.menubar.triggered[QtWidgets.QAction].connect(self.menufun)
        #myadding
        self.Wkitem=[]
        self.Batitem=[]
        self.Bowlitem=[]
        self.Allitem=[]
        self.choose=[]
        
        
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.radioButton.toggled.connect(self.checkstate)
        self.radioButton_2.toggled.connect(self.checkstate)
        self.radioButton_4.toggled.connect(self.checkstate)
        self.radioButton_3.toggled.connect(self.checkstate)

        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2) 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def checkstate(self):
        if self.radioButton_2.isChecked()==True:
            self.listWidget_2.clear()
            print(self.Batitem)
            self.listWidget_2.addItems(self.Batitem)
        elif self.radioButton.isChecked()==True:
            self.listWidget_2.clear()
            print(self.Wkitem)
            self.listWidget_2.addItems(self.Wkitem)
        elif self.radioButton_4.isChecked()==True:
            self.listWidget_2.clear()
            self.listWidget_2.addItems(self.Bowlitem)
        else:
            self.listWidget_2.clear()
            self.listWidget_2.addItems(self.Allitem)

    def menufun(self,action):
        print("Running....")
        txt=(action.text())
        print(txt)
        if txt=='New Team':
            self.reset()
            self.lineEdit_6.setText("100")
            self.lineEdit_5.setText("0")
            try:
                fdb1=sqlite3.connect('FantasyDB.db')
                cursr1=fdb1.cursor()
                cursr1.execute("SELECT Player,val,ctg from stats")
                while True:
                    record=cursr1.fetchone()
                    if record==None:
                        break
                    name=record[0]
                    val=record[1]
                    ctg=record[2]
                    print(name,val,ctg)
                    
                    item=""
                    item=item+name
                    for i in range(1,35-len(name)):
                        item=item+" "
                    item=item+str(val)
                    if ctg=='WK' and item not in self.Wkitem:
                        self.Wkitem.append(item)
                    elif ctg=='BAT':
                        print(name)
                        self.Batitem.append(item)
                    elif ctg=='AR':
                        self.Allitem.append(item)
                    else:
                        self.Bowlitem.append(item)
                       
                    self.radioButton.setChecked(True)
                self.listWidget_2.addItems(self.Wkitem)
                    
            except:
                print("Failed..")
        elif txt=='Save Team':
            self.saveteam()
        elif txt=='Evaluate Team' or txt=='Open Team':
            self.openNewWindow()

    def openNewWindow(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def saveteam(self):
        text, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Dream Team Selector', 'Enter name of team:')
        if ok:
            self.lineEdit_7.setText(str(text))
        selected=""
        cnt=self.listWidget.count()
        for i in range(cnt):
                tx=self.listWidget.item(i).text()
                cx=0
                res=""
                for e in tx:
                    if e==" " and cx==1:
                        break
                    elif e==" ":
                        res=res+" "
                        cx=cx+1
                    else:
                        res=res+e
                selected=selected+res
                if i<cnt-1:
                    selected=selected+","
        print(selected)
        fdb1=sqlite3.connect('FantasyDB.db')
        #cursr1=fdb1.cursor()
        print("had")
        name=text
        value=float(self.lineEdit_5.text())
        sql="INSERT INTO teams (name, players, value) VALUES ('{}','{}',{});".format(str(name),str(selected),str(value))
        print(sql)
        try:
            fdb1.execute(sql)
            fdb1.commit()
            QMessageBox.warning(None, "message","Added Succesfully")
            print("Run Sucessfully")
        except:
            #self.showdlg ("error in operation")
            print("Error")
            QMessageBox.warning(None, "message","Error!!!")
            fdb1.rollback()
        
    def removelist1(self, item):
        print("rmlist1  :")
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        vl=""
        cnt=0
        for e in item.text():
            if e!=" ":
                vl=vl+e
            elif cnt==1:
                break
            else:
                vl=vl+" "
                cnt=cnt+1;
        print(vl)
        
        fdb1=sqlite3.connect('FantasyDB.db')
        cursr1=fdb1.cursor()
        sql="SELECT val,ctg from stats WHERE Player='{}'".format(vl)
        print(sql)
        cursr1.execute(sql)
        val=cursr1.fetchone()
        print(val)
        prval=self.lineEdit_6.text()
        ltrval=self.lineEdit_5.text()
        print(prval,ltrval)
        prval=str(float(prval)-val[0])
        ltrval=str(float(ltrval)+val[0])
        if float(prval)<0.0:
             QMessageBox.warning(None, "Message", "You Can't Add this Player!!!")
             prval=str(float(prval)+val[0])
             ltrval=str(float(ltrval)-val[0])
        else:
            ctg=val[1]
            #1
            if ctg=='BAT' and self.edit1.text()=="":
                self.edit1.setText("1")
                self.listWidget.addItem(item.text())
                self.lineEdit_6.setText(prval)
                self.lineEdit_5.setText(ltrval)
                self.Batitem.remove(item.text())
                self.choose.append(item.text())
            elif ctg=='BAT':
                txt=self.edit1.text()
                txt=str(int(txt)+1)
                if int(txt)>5:
                    self.listWidget_2.addItem(item.text())
                    QMessageBox.warning(None, "Message", "You Can't Choose more than five Btasman!!")
                else:
                    self.edit1.setText(txt)
                    self.listWidget.addItem(item.text())
                    self.lineEdit_6.setText(prval)
                    self.lineEdit_5.setText(ltrval)
                    self.Batitem.remove(item.text())
                    self.choose.append(item.text())
            #2         
            if ctg=='BOWL' and self.edit2.text()=="":
               
                self.edit2.setText("1")
                self.listWidget.addItem(item.text())
                self.lineEdit_6.setText(prval)
                self.lineEdit_5.setText(ltrval)
                self.Bowlitem.remove(item.text())
                self.choose.append(item.text())
            elif ctg=='BOWL':
                txt=self.edit2.text()
                txt=str(int(txt)+1)
                if int(txt)>5:
                    self.listWidget_2.addItem(item.text())
                    QMessageBox.warning(None, "Message", "You Can't Choose more than five Btasman!!")
                else:
                    self.edit2.setText(txt)
                    self.listWidget.addItem(item.text())
                    self.lineEdit_6.setText(prval)
                    self.lineEdit_5.setText(ltrval)
                    self.Bowlitem.remove(item.text())
                    self.choose.append(item.text())
           #3
            if ctg=='WK' and self.edit4.text()=="" or self.edit4.text()=="0":
                #print("cddddd")
                self.edit4.setText("1")
                self.listWidget.addItem(item.text())
                self.lineEdit_6.setText(prval)
                self.lineEdit_5.setText(ltrval)
                self.Wkitem.remove(item.text())
                self.choose.append(item.text())
            elif ctg=="WK":
                self.listWidget_2.addItem(item.text())
                QMessageBox.warning(None, "Message", "You Can't Choose more than One WicketKeeper!!")

            #4
            if ctg=='AR' and self.edit3.text()=="":
                self.edit3.setText("1")
                self.listWidget.addItem(item.text())
                self.lineEdit_6.setText(prval)
                self.lineEdit_5.setText(ltrval)
                self.Allitem.remove(item.text())
                self.choose.append(item.text())
            elif ctg=='AR':
                txt=self.edit3.text()
                txt=str(int(txt)+1)
                if int(txt)>3:
                    self.listWidget_2.addItem(item.text())
                    QMessageBox.warning(None, "Message", "You Can't Choose more than Three AllRounder!!")
                else:
                    self.edit3.setText(txt)
                    self.listWidget.addItem(item.text())
                    self.lineEdit_6.setText(prval)
                    self.lineEdit_5.setText(ltrval)
                    self.Allitem.remove(item.text())
                    self.choose.append(item.text())
            print(len(self.choose))
            if len(self.choose)==11:
                msgbox = QMessageBox(QMessageBox.Question, "Save Team", " Save Your team from menu bar")
                msgbox.addButton(QMessageBox.Yes)
                msgbox.addButton(QMessageBox.No)
                msgbox.setDefaultButton(QMessageBox.No)
                msgbox.exec_()
                
       #
        
##        
##        
##
    
   
    def removelist2(self, item):
        self.listWidget.takeItem(self.listWidget.row(item))
        vl=""
        cnt=0
        for e in item.text():
            if e!=" ":
                vl=vl+e
            elif cnt==1:
                break
            else:
                vl=vl+" "
                cnt=cnt+1;
        print(vl)
        
        self.listWidget_2.addItem(item.text())
        fdb1=sqlite3.connect('FantasyDB.db')
        cursr1=fdb1.cursor()
        sql="SELECT val,ctg from stats WHERE Player='{}'".format(vl)
        print(sql)
        cursr1.execute(sql)
        val=cursr1.fetchone()
        print(val)
        prval=self.lineEdit_6.text()
        ltrval=self.lineEdit_5.text()
        print(prval,ltrval)
        prval=str(float(prval)+val[0])
        ltrval=str(float(ltrval)-val[0])

        if val[1]=='BAT':
            txt=self.edit1.text()
            txt=str(int(txt)-1)
            self.edit1.setText(txt)
            self.choose.remove(item.text())
            self.Batitem.append(item.text())
            self.lineEdit_6.setText(prval)
            self.lineEdit_5.setText(ltrval)
        if val[1]=='WK':
            txt=self.edit4.text()
            txt=str(int(txt)-1)
            self.edit4.setText(txt)
            self.choose.remove(item.text())
            self.Wkitem.append(item.text())
            self.lineEdit_6.setText(prval)
            self.lineEdit_5.setText(ltrval)
        
        if val[1]=='AR':
            txt=self.edit3.text()
            txt=str(int(txt)-1)
            self.edit3.setText(txt)
            self.choose.remove(item.text())
            self.Allitem.append(item.text())
            self.lineEdit_6.setText(prval)
            self.lineEdit_5.setText(ltrval)
            
        if val[1]=='BOWL':
            txt=self.edit2.text()
            txt=str(int(txt)-1)
            self.edit2.setText(txt)
            self.choose.remove(item.text())
            self.Bowlitem.append(item.text())
            self.lineEdit_6.setText(prval)
            self.lineEdit_5.setText(ltrval)
    def reset(self):
        self.edit1.setText("0")
        self.edit2.setText("0")
        self.edit3.setText("0")
        self.edit4.setText("0")
        self.lineEdit_6.setText("100")
        self.lineEdit_5.setText("0")
        self.listWidget.clear()
        self.listWidget_2.clear()
        while len(self.Wkitem) > 0 :
            self.Wkitem.pop()
        while len(self.Batitem) > 0 :
            self.Batitem.pop()
        while len(self.Bowlitem) > 0 :
            self.Bowlitem.pop()
        while len(self.Allitem) > 0 :
            self.Allitem.pop()
        while len(self.choose) > 0 :
            self.choose.pop()
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "BAT :"))
        self.label_5.setText(_translate("MainWindow", "BOWL :"))
        self.label_3.setText(_translate("MainWindow", "AR :"))
        self.label_2.setText(_translate("MainWindow", "WK :"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_7.setText(_translate("MainWindow", "Available Points :"))
        self.label_6.setText(_translate("MainWindow", "Used Points :"))
        self.radioButton_2.setText(_translate("MainWindow", "BAT"))
        self.radioButton_4.setText(_translate("MainWindow", "BOWL"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton.setText(_translate("MainWindow", "WK"))
        self.label_8.setText(_translate("MainWindow", "Team Name :"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams "))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

