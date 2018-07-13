#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.popup import Popup


class compo():

    def __init__(self, glay, ratio, label_1, label_2):
        self.ratio = ratio
        glay.add_widget(Label(text= label_1, font_name = 'HMFMPYUN'))
        self.intxt = TextInput(multiline = False)
        glay.add_widget(self.intxt)
        self.btn = Button(text = '변환하기', font_name = 'HMFMPYUN')
        glay.add_widget(self.btn)
        self.btn.bind(on_press = lambda x: self.OnClick(None))
        glay.add_widget(Label(text = label_2, font_name = 'HMFMPYUN'))
        self.outtxt = TextInput(readonly=True, multiline = False, focus=False)
        glay.add_widget(self.outtxt)


    def check(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

        
    def OnClick(self, a):
        if not self.check(self.intxt.text):
            Popup(title = 'Error!!', content=Label(text='정수/실수 값을 입력해 주십시오.', font_name = 'HMFMPYUN'), size_hint=(None, None), size=(200, 100)).open()
        else:
            self.outtxt.text = ('%.4f'%(float(self.intxt.text) * self.ratio))


class SimpleKivy(App):
    def build(self):
        self.ratios = [0.3025, 3.30579, 0.9144, 1.09361]
        self.label = ['평방미터', '평       ', '평       ', '평방미터', '야드     ', '미터     ', '미터     ', '야드     '] 
        layout = GridLayout(cols=5)
        for index in range(0, 4):
            compo(layout, self.ratios[index], self.label[index * 2], self.label[index * 2 + 1])
        return layout


if __name__ == "__main__":
    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '200')
    Config.write()
    
    SimpleKivy().run()
