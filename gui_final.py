# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#import pkg_resources.py2_warn
import re
from numba import cuda
import tensorflow as tf
from tensorflow import keras
import numpy as np
import functools
import os
import io
#from twitter_scraper import get_tweets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from requests_html import HTML, HTMLSession
from langdetect import detect

import tweepy 
import json

#configuring twitter  api
consumerKey = "WL9qLoAs3iITSoA0Ywk0P3HlS" 
consumerSecret = "rzZMPzjsLqFu92IVOJjjIJBeEEgNE9XyrC1ynp9jN2RsiV3fDa" 
accessToken = "1120882257118420992-moWBx8bFzxYKU83Z6Ozkwpub9Y2Km9" 
accessTokenSecret = "TY4qwgQ8MDNpfqDYGh4fTwNYOaSf31HbWtDp9Datp2iLP" 
 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret) 
auth.set_access_token(accessToken, accessTokenSecret) 
api = tweepy.API(auth) 
india_trends = api.trends_place(2282863)

#print(json.dumps(india_trends, indent=4))


def get_trends():
    india_trends_set = set([trend['name'] 
                        for trend in india_trends[0]['trends']])
    
    #set to list
    india_trends_list = list(india_trends_set) 
    return india_trends_list

def get_tweets(tag):
    q = tag
    date_since = "2020-12-7"
    tweets = tweepy.Cursor(api.search,
                q=q,
                lang="en",
                since=date_since).items(100)
    return tweets




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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 591, 31))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 591, 31))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 450, 211, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 450, 221, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(190, 81, 591, 321))
        self.textBrowser.setObjectName("textBrowser")
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
        self.button1.setText(_translate("MiniProject", "PushButton"))
        self.button2.setText(_translate("MiniProject", "PushButton"))
        self.button3.setText(_translate("MiniProject", "PushButton"))
        self.button4.setText(_translate("MiniProject", "PushButton"))
        self.button5.setText(_translate("MiniProject", "PushButton"))
        self.button6.setText(_translate("MiniProject", "PushButton"))
        self.button7.setText(_translate("MiniProject", "PushButton"))
        self.button8.setText(_translate("MiniProject", "PushButton"))
        self.button9.setText(_translate("MiniProject", "PushButton"))
        self.button10.setText(_translate("MiniProject", "PushButton"))
        self.runbutton.setText(_translate("MiniProject", "RUN"))
        self.label.setText(_translate("MiniProject", ""))
        self.label_2.setText(_translate("MiniProject", ""))
        self.pushButton.setText(_translate("MiniProject", "reset"))
        self.pushButton_2.setText(_translate("MiniProject", "Flush Gpu"))
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
        self.pushButton.clicked.connect(self.clickedreset)
        self.pushButton_2.clicked.connect(self.show_popup)

    def clickedreset(self):
        self.textBrowser.setText(" ")
    def clickedresetgpu(self, i):
        device = cuda.get_current_device()
        device.reset()
        QApplication.quit()
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Are you sure !")
        msg.setText("Window will close")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        msg.buttonClicked.connect(self.clickedresetgpu)
        x = msg.exec_()
        


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
        except ConnectionError :
            self.label.setText("ERROR 101")


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
        self.textBrowser.setText("tweets-----------------")
        for tweet in get_tweets(tag):
            text = tweet.text
            mline = clean_tweet(text)
            nline = mline.replace("," , "").replace("." , "").replace(")" , "").replace("(" , "").replace(";" , "").replace(":" , "").replace("\"" , " ").strip().split(" ")
            encode = review_encode(nline)
            encode = keras.preprocessing.sequence.pad_sequences([encode],value=word_index["<PAD>"],padding="post",maxlen=250)
            predict = model.predict(encode)
            listtostr = ' '.join([str(elem) for elem in nline])
            self.textBrowser.append("#    "+listtostr)
            if listtostr.lower().find("pride") == True:
                mean = mean + 100
            if listtostr.lower().find("congratulations") == True:
                mean = mean + 100
            mean = ( mean + predict[0])
            total = total + 1
        try:
            mean_final = mean / total 

            if mean_final * 100 >= 50 :
                #print("POSITIVE")
                #print(mean_final)
                self.label_2.setText("POSITIVE : "+str(mean_final * 100))
            elif mean_final * 100 >= 40 and mean_final * 100 <= 50 :
                #print("Negative")
                #print(mean_final)
                self.label_2.setText("Sadness : "+ str(mean_final * 100))
            elif mean_final * 100 >= 30 and mean_final * 100 <= 40 :
                #print("Negative")
                #print(mean_final)
                self.label_2.setText("Mild Anger : "+ str(mean_final * 100))
            elif mean_final * 100 >= 20 and mean_final * 100 <= 30  :
                #print("Negative")
                #print(mean_final)
                self.label_2.setText("Anger : "+ str(mean_final * 100))
            elif mean_final * 100 >= 1 and mean_final * 100 <= 20  :
                #print("Negative")
                #print(mean_final)
                self.label_2.setText("Extreme Anger : "+ str(mean_final * 100))
        except ValueError:
            self.label.setText("Valuse ERROR")















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MiniProject = QtWidgets.QMainWindow()
    ui = Ui_MiniProject()
    ui.setupUi(MiniProject)
    MiniProject.show()
    sys.exit(app.exec_())