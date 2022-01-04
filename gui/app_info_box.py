import tkinter as tk
from tkinter import Text

class AppInfoBox(Text):
    
    def __init__(self, master=None, row=0, column=1, width=15, height=15, padx=5, pady=5):
        super().__init__(master = master, width = width, height = height)

        self.grid(row=row, column=column, padx = padx, pady = pady)
        self.config(state='disabled')

    def write(self, text):
        self.configure(state='normal')
        self.delete('1.0', tk.END)
        self.insert(tk.INSERT, text)
        self.configure(state='disabled')