from tkinter import Label, Tk, Entry, Button, Text

class GUI:
    def __init__(self, title="Aplicación", dimensions="1200x600"):
        self.create_window(title=title, dimensions=dimensions)

    def create_window(self, title, dimensions):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(dimensions)

    def create_label(self, text='label', height=2, width=15, row=0, column=0, master=None, padx=5, pady=20):
        label = Label(
            master = master,
            height = height, 
            width = width,
            text = text
        )

        label.grid(row=row, column=column, padx = padx, pady = pady)
        return label

    def create_entry(self, text='', width=15, row=0, column=1, master=None, padx=5, pady=5):
        entry = Entry(
            master = master,
            width = width,
            text = text
        )

        entry.grid(row=row, column=column, padx = padx, pady = pady)

    def create_button(self, func, name, height=2, width=15, row=0, column=1, master=None, padx=5, pady=5):

        button = Button(
            master = master, 
            command = func,
            height = height, 
            width = width,
            text = name
        )
        
        button.grid(row=row, column=column, padx = padx, pady = pady)
        return button

    def create_text(self, text='', width=15, height=15, row=0, column=1, master=None, padx=5, pady=5):
        text = Text(
            master = master,
            width = width,
            height = height
        )

        text.grid(row=row, column=column, padx = padx, pady = pady)
        text.config(state='disabled')

        return text

    def run_gui(self):
        self.window.mainloop()
