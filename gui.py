#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wxk on 2018/4/2 下午7:20
# Email="wangxk1991@gamil.com"
# Desc: gui界面
import os
import sys
from tkinter import *
import tkinter.messagebox


class SelectFrame():
    def buttonListener(self, event):
        tkinter.messagebox.showinfo("messagebox", "this is button 1 dialog")
        self.frame.quit()

    def __init__(self, selects):
        self.frame = Tk()

        i = 1
        label = Label(self.frame, text="其从如下的连接中选择一个：", width=40, height=3)
        label.grid(row=0, column=0, padx=1, pady=5)
        for sel in selects:
            i += 1
            label = Label(self.frame, text=sel, width=40, height=3)
            label.grid(row=i, column=0, padx=1, pady=5)
            for server in selects[sel]:
                if server != "" and server != None:
                    button = Button(self.frame, text=server, width=40, height=1)
                    button.grid(row=i, column=0, padx=1, pady=1)
                    button.bind("<ButtonRelease>", self.buttonListener)
                    i += 1

        self.frame.mainloop()
