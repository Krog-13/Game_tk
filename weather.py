import tkinter as tk
from apii import Sel_Country
'''
Программа выводит температуру и скорость ветра любого города из KZ и RU
'''

class Country:

    def __init__(self, master):
        self.master = master
        self.var = tk.IntVar()
        self.var.set(0)
        self.cities = []
        tk.Radiobutton(self.master, text='Russian', variable=self.var, value=1, command=self.select_country).pack(anchor='w')
        tk.Radiobutton(self.master, text='Kazakhstan', variable=self.var, value=2, command=self.select_country).pack(anchor='w')

    def select_country(self):
        '''
        по нажатию чекбокса передает в модуль apii
        страну которую выбрали
        получаем списко городов этой страны
        '''
        if self.var.get() == 1:
            a = Sel_Country('RU')
            self.cities = a.selection()
        elif self.var.get() == 2:
            a = Sel_Country('KZ')
            self.cities = a.selection()
        else:
            print('error')


class Entry(Country):

    def __init__(self, master):
        super().__init__(master)
        tk.Button(self.master, text='Add', command = self.add_list_cities).pack(anchor='w')
        self.lable = tk.Label(self.master, bg='brown', fg='white', width=20, text=' ', anchor='nw')
        self.lable.pack()
        self.entry = tk.Entry(self.master, width=20, justify='left')
        self.entry.pack()
        tk.Button(self.master, text='PUSH', command = self.get_ciry).pack()
        self.listbox = tk.Listbox(self.master)
        self.listbox.pack()
        tk.Button(self.master, text='reset', command = self.list_reset).pack()

    def add_list_cities(self):
        #добаление списка городов
        for item in self.cities:
            self.listbox.insert(tk.END, item)

    def list_reset(self):
        #сброс списка городов
        self.listbox.delete(0, tk.END)

    def get_ciry(self):
        #---
        city = self.entry.get()
        try:
            a = Sel_Country.cities('',city)
        except Exception as Exc:
            print(f'Ошибка в название города {city}, ошибка {Exc}')
        self.lable['text'] = a[0],'Degrees', a[1], 'm/c'

#initialization
def main():
    root = tk.Tk()
    root.geometry('500x400')
    app = Entry(root)
    root.mainloop()

if __name__ == '__main__':
    main()
