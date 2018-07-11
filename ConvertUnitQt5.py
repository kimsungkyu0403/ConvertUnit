#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize

class ConvertUnit(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ConvertUnit')
        self.setGeometry(10, 10, 400, 200)
 
        self.horizontalGroupBox = QGroupBox("단위변환기")
        
        self.widgets = [[],[],[],[]]
        self.ratios = [0.3025, 3.30579, 0.9144, 1.09361]
        self.label = ['평방미터', '평       ', '평       ', '평방미터', '야드     ', '미터     ', '미터     ', '야드     ']
        
        
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        
        for index in range(0, 4):
            self.widgets[index].append(QLabel(self.label[index * 2]))
            self.widgets[index].append(QLineEdit())
            self.widgets[index].append(QPushButton('변환하기', self))
            self.widgets[index][2].clicked.connect(lambda arg1 = index: self.onClick(arg1))
            self.widgets[index].append(QLabel(self.label[index * 2 + 1]))
            self.widgets[index].append(QLineEdit())
            self.widgets[index][4].setDisabled(True)
            
            for i in range(0, 5):
                layout.addWidget(self.widgets[index][i], index, i)

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
