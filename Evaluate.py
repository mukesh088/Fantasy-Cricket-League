# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 456)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 70, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 70, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 61, 16))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(80, 121, 256, 281))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 420, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 420, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #my add
        self.pushButton.clicked.connect(self.calculateScore)
        fdb1=sqlite3.connect('FantasyDB.db')
        cursr1=fdb1.cursor()
        sql="SELECT name from teams"
        cursr1.execute(sql)
        while True:
            record=cursr1.fetchone()
            if record==None:
                break
            self.comboBox.addItem(record[0])
        cursr1.execute("")
        self.comboBox_2.addItem("Match1")
        
        self.comboBox.activated.connect(self.addteam)

        #self.cScore=self.addteam()
        
        

        self.list1=[]
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def calculateScore(self):
        QMessageBox.information(None, "Message", "You Total Score is {}".format(self.cScore))

    def addteam(self):
        self.listWidget.clear()
        indx=self.comboBox.currentIndex()
        text=self.comboBox.currentText()
        fdb1=sqlite3.connect('FantasyDB.db')
        cursr1=fdb1.cursor()
        sql="SELECT Players from teams WHERE name='{}'".format(text)
        cursr1.execute(sql)
        record=cursr1.fetchone()
        print(record[0])
        plyr=""
        x=0
        sr=record[0]
        total=0.0
        #print(len(sr),len(record[0]))
        for i in record[0]:
            if i==',':
                cursr1.execute("Select * FROM match WHERE Player='{}'".format(plyr))
                result=cursr1.fetchone()
                rns=result[1]
                bls=result[2]
                f=result[3]
                s=result[4]
                bld=result[5]
                md=result[6]
                rnc=result[7]
                wkt=result[8]
                ctch=result[9]
                stmp=result[10]
                ro=result[11]
                scr=self.score(rns,bls,f,s,bld,md,rnc,wkt,ctch,stmp,ro)
                #print(plyr,scr)
                item=""
                item=item+plyr
                for i in range(1,35-len(plyr)):
                    item=item+" "
                item=item+str(scr)
                self.listWidget.addItem(item)
                print(item)
                total=total+scr
                plyr=""
                continue
            else:
                plyr=plyr+i
            
        cursr1.execute("Select * FROM match WHERE Player='{}'".format(plyr))
        result=cursr1.fetchone()
        rns=result[1]
        bls=result[2]
        f=result[3]
        s=result[4]
        bld=result[5]
        md=result[6]
        rnc=result[7]
        wkt=result[8]
        ctch=result[9]
        stmp=result[10]
        ro=result[11]
        scr=self.score(rns,bls,f,s,bld,md,rnc,wkt,ctch,stmp,ro)
        #print(plyr,scr)
        item=""
        item=item+plyr
        for i in range(1,35-len(plyr)):
            item=item+" "
        item=item+str(scr)
        self.listWidget.addItem(item)
        print(item)
        total=total+scr
        self.cScore=total
        
    def score(self,r,b,f,s,bl,md,rnsc,wkt,ctch,stmp,ro):
        runs=r
        points=(float)(runs/2)
        if runs>=100:
            points=points+10
        elif runs>=50:
            points=points+5
        try:
            if (float)(runs/b)>=0.8 and  (float)(runs/b)<=1.0:
                points=points+2
            elif (float)(runs/b)>1.0:
                points=points+2
        except:
             pass
        points=points+1*f+2*s+10*wkt+10*ctch+10*stmp+10*ro
        if wkt>=5:
            points=points+10
        elif wkt>=3:
            points=points+5
        try:
            over=(float)(bl/6)
            if (float)(rnsc/over)>=3.5 and (float)(rnsc/over)<=4.5:
                points=points+4
            elif (float)(rnsc/over)>=2 and (float)(rnsc/over)<3.5:
                points=points+7
            elif (float)(rnsc/over)<2:
                points=points+10
        except:
            pass
        return points
        
        
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate The Performance of Your Team"))
        self.label_2.setText(_translate("Form", "Select Team"))
        self.label_3.setText(_translate("Form", "Select Match"))
        self.pushButton.setText(_translate("Form", "Calculate Score"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

