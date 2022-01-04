from tkinter import Tk

class GUI:
    def __init__(self, title="Aplicación", dimensions="1500x600"):
        self.create_window(title=title, dimensions=dimensions)

    def create_window(self, title, dimensions):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(dimensions)

    def run_gui(self):
        self.window.mainloop()
