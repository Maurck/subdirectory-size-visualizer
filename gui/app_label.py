from tkinter import Label

class AppLabel(Label):
    def __init__(self, master=None, row=0, column=0, text='label', height=2, width=15,  padx=5, pady=20):
        super().__init__(
            master = master,
            height = height, 
            width = width,
            text = text
        )

        self.grid(row=row, column=column, padx = padx, pady = pady)