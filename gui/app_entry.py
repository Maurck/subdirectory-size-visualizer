from tkinter import Entry

class AppEntry(Entry):
    def __init__(self, master=None, row=0, column=0, text='', width=15, padx=5, pady=5):
        
        super().__init__(
            master = master,
            width = width,
            text = text
        )

        self.grid(row=row, column=column, padx = padx, pady = pady)

