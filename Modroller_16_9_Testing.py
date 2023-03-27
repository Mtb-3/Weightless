from pyautogui import *
import pyautogui 
import time 
import keyboard
import random 
import win32api, win32con
import pydirectinput as pyd
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLineEdit, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout, QSlider, QMessageBox)
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
import requests
import re
import os
import sys



class DialogApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Weightless'
        self.setWindowIcon(QtGui.QIcon('bluefeather.jpg'))
        self.left = 300
        self.top = 50
        self.width = 265
        self.height = 100
        self.initUI()
           

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.button_roll = QPushButton('Roll for mod',self)
        self.button_roll.move(20,15)
        self.button_roll.clicked.connect(self.click_func)
        
        self.button_roll_4k = QPushButton("Roll mod 4k",self)
        self.button_roll_4k.move(20,60)
        self.button_roll_4k.clicked.connect(self.click_func_4k)

        self.button_fusing = QPushButton('Fusing/Jewel',self)
        self.button_fusing.move(140,40)
        self.button_fusing.clicked.connect(self.fusing_func)
        
        self.button_howto = QPushButton('?',self)
        self.button_howto.move(240,0)
        self.button_howto.resize(25,25)
        self.button_howto.clicked.connect(self.help)

        

    def click_func(self):
        time.sleep(3.00)
        
        while keyboard.is_pressed('alt') == False:      
            pyd.PAUSE = 0.1
            pyd.keyDown('shift')
            pyd.leftClick()
            
            pic = pyautogui.screenshot(region=(40, 0, 515, 805))
            width, height = pic.size
            for x in range(0,width,5):
                for y in range(0,height,5):

                    r,g,b = pic.getpixel((x,y))

                    if r == 231 and g == 180 and b == 119:
                        time.sleep(2.00)
                        pyd.keyUp('shift')
                        return
        pyd.keyUp('shift')
        
    def click_func_4k(self):
        time.sleep(3.00)
        
        while keyboard.is_pressed('alt') == False:      
            pyd.PAUSE = 0.1
            pyd.keyDown('shift')
            pyd.leftClick()
            
            pic = pyautogui.screenshot(region=(80, 0, 1030, 1610))
            width, height = pic.size
            for x in range(0,width,5):
                for y in range(0,height,5):

                    r,g,b = pic.getpixel((x,y))

                    if r == 231 and g == 180 and b == 119:
                        time.sleep(2.00)
                        pyd.keyUp('shift')
                        return
        pyd.keyUp('shift')


    def fusing_func(self):
        time.sleep(3.00)
        while keyboard.is_pressed('alt') == False:
            pyd.PAUSE = 0.01
            pyd.keyDown('shift')
            pyd.leftClick()

            pic = pyautogui.screenshot(region=(705, 550, 300, 305))

            width, height = pic.size

            for x in range(0,width,5):
                for y in range(0,height,5):

                    r,g,b = pic.getpixel((x,y))

                    if r == 49 and g == 110 and b == 18:
                        time.sleep(2.00)
                        pyd.keyUp('shift')
                        return
        pyd.keyUp('shift')
        
                                     

    def help(self):
        msg = QMessageBox()
        msg.setTextFormat(Qt.RichText)
        font = msg.font()
        font.setPointSize(12)
        msg.setFont(font)
        msg.setWindowTitle('Help')
        msg.setText("The roll for mod button only works in the currency stash tab. Type the mod you want to roll in the currency tab text box. There is a 3 second delay until the program begins.1. Click correct roll for mod button based on your resolution. 2. Choose currency 3. Mouseover item. 4. Program ends once mod is found. Hold 'alt' to stop program.")
        msg.exec_()
        
               
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogApp()
    demo.show()
    sys.exit(app.exec_()) 
