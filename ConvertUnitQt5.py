#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize

class ConvertUnit(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'ConvertUnit'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 200

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.horizontalGroupBox = QGroupBox("단위변환기")
        
        self.widgets = [[],[],[],[]]
        self.ratios = [0.3025, 3.30579, 0.9144, 1.09361]
        self.label = ['평방미터', '평       ', '평       ', '평방미터', '야드     ', '미터     ', '미터     ', '야드     ']
        
        
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        
        for index in range(0, 4):
            self.lbl1 = QLabel(self.label[index * 2])
            self.widgets[index].append(self.lbl1)
            
            self.txt1= QLineEdit()
            self.widgets[index].append(self.txt1)
            
            self.btn = QPushButton('변환하기', self)
            self.btn.clicked.connect(lambda arg1 = index: self.onClick(arg1))
            self.widgets[index].append(self.btn)
            
            self.lbl2 = QLabel(self.label[index * 2 + 1])
            self.widgets[index].append(self.lbl2)
            
            self.txt2 = QLineEdit()
            self.txt2.setDisabled(True)
            self.widgets[index].append(self.txt2)
            
            layout.addWidget(self.widgets[index][0], index, 0)
            layout.addWidget(self.widgets[index][1], index, 1)
            layout.addWidget(self.widgets[index][2], index, 2)
            layout.addWidget(self.widgets[index][3], index, 3)
            layout.addWidget(self.widgets[index][4], index, 4)

        self.horizontalGroupBox.setLayout(layout)
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

    def check(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    def onClick(self, index):
        if not self.check(self.widgets[index][1].text()):
            QMessageBox.about(self, "에러!!", "입력된 값이 정수/실수가 아닙니다.")
        else:
            self.widgets[index][4].setText(str('%.4f'% (float(self.widgets[index][1].text()) * self.ratios[index])))


if __name__ == '__main__':
    app = QApplication (sys.argv)
    ex = ConvertUnit()
    ex.show()
    sys.exit (app.exec_())
