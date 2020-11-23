# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import re
import tensorflow as tf
from tensorflow import keras
import numpy as np
import functools
import os
import io
from twitter_scraper import get_tweets, get_trends
from PyQt5 import QtCore, QtGui, QtWidgets
from requests_html import HTML, HTMLSession
from langdetect import detect


class Ui_MiniProject(object):
    def setupUi(self, MiniProject):
        MiniProject.setObjectName("MiniProject")
        MiniProject.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MiniProject)
        self.centralwidget.setObjectName("centralwidget")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.button1.setObjectName("button1")

        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(0, 40, 171, 41))
        self.button2.setObjectName("button2")

        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(0, 80, 171, 41))
        self.button3.setObjectName("button3")

        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(0, 120, 171, 41))
        self.button4.setObjectName("button4")

        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(0, 160, 171, 41))
        self.button5.setObjectName("button5")

        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(0, 200, 171, 41))
        self.button6.setObjectName("button6")

        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(0, 240, 171, 41))
        self.button7.setObjectName("button7")

        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(0, 280, 171, 41))
        self.button8.setObjectName("button8")

        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(0, 320, 171, 41))
        self.button9.setObjectName("button9")

        self.button10 = QtWidgets.QPushButton(self.centralwidget)
        self.button10.setGeometry(QtCore.QRect(0, 360, 171, 41))
        self.button10.setObjectName("button10")

        self.runbutton = QtWidgets.QPushButton(self.centralwidget)
        self.runbutton.setGeometry(QtCore.QRect(0, 450, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.runbutton.setFont(font)
        self.runbutton.setObjectName("runbutton")

        self.checkbutton = QtWidgets.QPushButton(self.centralwidget)
        self.checkbutton.setGeometry(QtCore.QRect(280, 450, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkbutton.setFont(font)
        self.checkbutton.setObjectName("checkbutton")

        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setGeometry(QtCore.QRect(530, 450, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resetbutton.setFont(font)
        self.resetbutton.setObjectName("resetbutton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 591, 31))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 591, 351))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")

        MiniProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MiniProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")

        MiniProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MiniProject)
        self.statusbar.setObjectName("statusbar")
        MiniProject.setStatusBar(self.statusbar)

        self.retranslateUi(MiniProject)
        QtCore.QMetaObject.connectSlotsByName(MiniProject)

    def retranslateUi(self, MiniProject):
        _translate = QtCore.QCoreApplication.translate
        MiniProject.setWindowTitle(_translate("MiniProject", "MiniProject"))
        self.button1.setText(_translate("MiniProject", ""))
        self.button2.setText(_translate("MiniProject", ""))
        self.button3.setText(_translate("MiniProject", ""))
        self.button4.setText(_translate("MiniProject", ""))
        self.button5.setText(_translate("MiniProject", ""))
        self.button6.setText(_translate("MiniProject", ""))
        self.button7.setText(_translate("MiniProject", ""))
        self.button8.setText(_translate("MiniProject", ""))
        self.button9.setText(_translate("MiniProject", ""))
        self.button10.setText(_translate("MiniProject", ""))
        self.runbutton.setText(_translate("MiniProject", "RUN"))
        self.label.setText(_translate("MiniProject", ""))
        self.label_2.setText(_translate("MiniProject", ""))
        
        self.runbutton.clicked.connect(self.clicked)
        self.button1.clicked.connect(self.selection1)
        self.button2.clicked.connect(self.selection2)
        self.button3.clicked.connect(self.selection3)
        self.button4.clicked.connect(self.selection4)
        self.button5.clicked.connect(self.selection5)
        self.button6.clicked.connect(self.selection6)
        self.button7.clicked.connect(self.selection7)
        self.button8.clicked.connect(self.selection8)
        self.button9.clicked.connect(self.selection9)
        self.button10.clicked.connect(self.selection10)


    var = []
    def clicked(self):
        self.label.setText("running...")
        self.var = get_trends()
        try:
            
            self.label.setText("TAG Extraction Finished!  Select Tag to Analyse")
            self.button1.setText(self.var[0])
            self.button2.setText(self.var[1])
            self.button3.setText(self.var[2])
            self.button4.setText(self.var[3])
            self.button5.setText(self.var[4])
            self.button6.setText(self.var[5])
            self.button7.setText(self.var[6])
            self.button8.setText(self.var[7])
            self.button9.setText(self.var[8])
            self.button10.setText(self.var[9])
        except:
            self.label.setText("ERROR 101")
        finally:
            self.label_2.setText("Wait...")

    def selection(self,tagtext):
        self.label.setText(tagtext)
        self.label_2.setText("Checking...")
        self.runningmodel(tagtext)

    def selection1(self):
        self.label.setText(self.var[0])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[0])
    
    def selection2(self):
        self.label_2.setText("Checking...")
        self.label.setText(self.var[1])
        self.runningmodel(self.var[1])

    def selection3(self):
        self.label.setText(self.var[2])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[2])
    
    def selection4(self):
        self.label.setText(self.var[3])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[3])
    
    def selection5(self):
        self.label.setText(self.var[4])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[4])

    def selection6(self):
        self.label.setText(self.var[5])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[5])
    
    def selection7(self):
        self.label.setText(self.var[6])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[6])

    def selection8(self):
        self.label.setText(self.var[7])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[7])

    def selection9(self):
        self.label.setText(self.var[8])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[8])

    def selection10(self):
        self.label.setText(self.var[9])
        self.label_2.setText("Checking...")
        self.runningmodel(self.var[9])

    def runningmodel(self,tag):
       
        def clean_tweet(tweet): 
            return ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\[\])", " ", tweet))


        def review_encode(s):
            encoded = [1]
            for word in s:
                if word.lower() in word_index:
                    encoded.append(word_index[word.lower()])
                else:
                    encoded.append(2)
            return encoded
        word_index = tf.keras.datasets.imdb.get_word_index()


        word_index = {k:(v+3) for k,v in word_index.items()}
        word_index["<PAD>"] = 0
        word_index["<START>"] = 1
        word_index["<UNK>"] = 2
        word_index["<UNUSED>"] = 3
        #reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])


        model = keras.models.load_model("model_final.h5")
        mean = 0
        total = 0
        for tweet in get_tweets(tag, pages=1):
            text = tweet['text']
            mline = clean_tweet(text)
            nline = mline.replace("," , "").replace("." , "").replace(")" , "").replace("(" , "").replace(";" , "").replace(":" , "").replace("\"" , " ").strip().split(" ")
            encode = review_encode(nline)
            encode = keras.preprocessing.sequence.pad_sequences([encode],value=word_index["<PAD>"],padding="post",maxlen=250)
        
            predict = model.predict(encode)
            #print(line)
            #print(mline)
            #print(encode)
            #print(predict[0])
            mean = ( mean + predict[0])
            total = total + 1

        mean_final = mean / total 

        if mean_final * 100 >= 50 :
            #print("POSITIVE")
            #print(mean_final)
            self.label_2.setText("positive")
        else :
            #print("Negative")
            #print(mean_final)
            self.label_2.setText("negative")

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MiniProject = QtWidgets.QMainWindow()
    ui = Ui_MiniProject()
    ui.setupUi(MiniProject)
    MiniProject.show()
    sys.exit(app.exec_())