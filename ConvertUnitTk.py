#!/usr/bin/emy python
#-*- encoding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

widgets = [[],[],[],[]]
ratios = [0.3025, 3.30579, 0.9144, 1.09361]
label = ['평방미터', '평       ', '평       ', '평방미터', '야드     ', '미터     ', '미터     ', '야드     ']


def check(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def onClick(index):
    if not check(widgets[index][1].get()):
        messagebox.showerror("에러!!", "입력된 값이 정수/실수가 아닙니다.")
    else: 
        widgets[index][4].configure(state = 'enabled')
        widgets[index][4].delete(0, END)
        widgets[index][4].insert(INSERT, float(widgets[index][1].get()) * ratios[index])
        widgets[index][4].configure(state = 'disabled')


def main():
    window = Tk()
    window.geometry("400x200")
    window.title("단위 변환기")
    Label(window, text = "단위 변환기", font = ('Arial Bold', 30)).grid(row = 0, columnspan = 5, padx = 5, pady = 5)

    for index in range(0, 4):                                                                          
        widgets[index].append(Label(window, text = label[index * 2]))
        widgets[index].append(Entry(window, width = 10, state = 'enabled'))
        widgets[index].append(Button(window, text = '변환하기', command = lambda arg1 = index:onClick(arg1)))
        widgets[index].append(Label(window, text = label[index * 2 + 1]))
        widgets[index].append(Entry(window, width = 10, state = 'disabled'))

    for row in range(1, 5):
        for column in range(0, 5):
            widgets[row - 1][column].grid(row = row, column = column, padx = 5, pady = 3)

    window.mainloop()


if __name__ == '__main__':
    status = main()
    exit(status)
