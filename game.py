import time
import tkinter as tk
import json
from random import randint
import datetime

class Block:
    def __init__(self, master):
        self.e = tk.Entry(root, width=20, justify='left')
        self.b = tk.Button(root, text='PUSH')
        self.l = tk.Label(root, bg='brown', fg='white', width=20, text='hear', anchor='nw')

        self.f_top = tk.Frame(master)
        self.l.pack(side='top')
        self.e.pack(side='top', expand=1)
        self.b.pack(side='top', ipadx=8, ipady=8)

        self.name = []
        self.count = 1

        self.inf = tk.Label(self.f_top, bg='green', fg='white', width=15, text='**')
        self.inf.pack(side='left')
        self.f_top.pack()


    def name_girl(self):
        self.name.append(self.e.get())
        self.l['text'] = 'done'
        with open('player.json', 'w') as file:
            json.dump(self.name, file, default=lambda odj: odj.__dect__)


    def setfun(self, func):
        self.b['command'] = eval('self.' + func)
        return (f'ostatok {self.name}')



class check(Block):
    def __init__(self, master):
        super().__init__(master)
        self.check = []
        self.name = ''
    def guess(self):
        with open ('player.json', 'r') as read:
            self.check = json.load(read)
        self.name = self.e.get()
        if self.checks():
            self.info()
        else:
            self.inf['text'] = "You aren't gussed"


    def setfun(self, func):
        self.b['command'] = eval('self.' + func)
        return (f'ostatok {self.name}')

    def checks(self):
        for i in range(len(self.check)):
            if self.check[i] == self.name:
                return True
            else:
                pass
    def info(self):
        self.inf['text'] = 'You are gussed'



root = tk.Tk()
root.geometry('500x350')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
first_block = Block(root)
first_block.setfun('name_girl')
first = check(root)
first.setfun('guess')

root.mainloop()