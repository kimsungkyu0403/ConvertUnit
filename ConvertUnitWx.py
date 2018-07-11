#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class ConvertUnit(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.widgets = [[],[],[],[]]
        self.ratios = [0.3025, 3.30579, 0.9144, 1.09361]
        self.label = ['평방미터', '평       ', '평       ', '평방미터', '야드     ', '미터     ', '미터     ', '야드     '] 

        self.panel = wx.Panel(self)     

        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        self.sizer = wx.GridBagSizer(5, 5)

        for index in range(0, 4):
            self.widgets[index].append(wx.StaticText(self.panel, label = self.label[index * 2]))
            self.widgets[index].append(wx.TextCtrl(self.panel))
            self.widgets[index].append(wx.Button(self.panel, label = '변환하기'))
            self.widgets[index][2].Bind(wx.EVT_BUTTON, lambda event, arg1=index: self.OnClick(event, arg1))
            self.widgets[index].append(wx.StaticText(self.panel, label = self.label[index * 2 + 1]))
            self.widgets[index].append(wx.TextCtrl(self.panel))
            self.widgets[index][4].Disable()
            for i in range (0, 5):
                self.sizer.Add(self.widgets[index][i], (index, i))

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)

    def Check(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def OnClick(self, event, index):
        if not self.Check(self.widgets[index][1].GetValue()):
            wx.MessageBox('정수/실수 값을 입력해 주십시오.', '에러!!', wx.OK | wx.ICON_INFORMATION)
        else:
            self.widgets[index][4].SetLabel(str('%.4f'%(float(self.widgets[index][1].GetValue()) * self.ratios[index])))

def main():

    app = wx.App(False)
    frame = ConvertUnit(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()