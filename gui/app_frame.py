from tkinter import Frame
import tkinter as tk

class AppFrame(Frame):
    def __init__(self, master=None, row=0, column=0):
        super().__init__(master)
        self.grid(row=row, column=column, sticky=tk.N)

