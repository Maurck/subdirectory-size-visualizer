from tkinter import Button

class AppButton(Button):
    def __init__(self, master=None, row=0, column=0, name=f'', func=None, height=2, width=15, padx=5, pady=5):

        super().__init__(
            master = master, 
            command = func,
            height = height, 
            width = width,
            text = name
        )
        
        self.grid(row=row, column=column, padx = padx, pady = pady)