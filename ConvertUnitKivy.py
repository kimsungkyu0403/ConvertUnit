#!/usr/bin/env python
# coding: utf-8

import kivy
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
import os


class ConvertUnit(GridLayout):
    
    def __init__(self, **kwargs):
        super(ConvertUnit, self).__init__(**kwargs)
        
        self.widgets = [[],[],[],[]]
        self.ratios = [0.3025, 3.30579, 0.9144, 1.09361]
        self.label = ['평방미터', '평       ', '평       ', '평방미터', '야드     ', '미터     ', '미터     ', '야드     '] 
        
        self.cols = 5
        
        for index in range(0, 4):
            self.widgets[index].append(Label(text= self.label[index * 2], font_name = 'HMFMPYUN'))
            self.widgets[index].append(TextInput(multiline = False))
            self.widgets[index].append(Button(text = '변환하기', font_name = 'HMFMPYUN'))
            self.widgets[index][2].bind(on_press = lambda arg1 = self.widgets[index][2], arg2 = index: self.OnClick(arg1, arg2))
            self.widgets[index].append(Label(text = self.label[index * 2 + 1], font_name = 'HMFMPYUN'))
            self.widgets[index].append(TextInput(readonly=True, multiline = False, focus=False))
                        
            for i in range(0, 5):
                self.add_widget(self.widgets[index][i])


    def check(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def OnClick(self, Btn, index):
        if not self.check(self.widgets[index][1].text):
            Popup(title = 'Error!!', content=Label(text='정수/실수 값을 입력해 주십시오.', font_name = 'HMFMPYUN'), size_hint=(None, None), size=(200, 100)).open()
        else:
            self.widgets[index][4].text = ('%.4f'%(float(self.widgets[index][1].text) * self.ratios[index]))


class SimpleKivy(App):
    def build(self):
        return ConvertUnit()


if __name__ == "__main__":
    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '200')
    Config.write()
    
    SimpleKivy().run()