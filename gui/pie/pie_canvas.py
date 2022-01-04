import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.figure

class PieCanvas(FigureCanvasTkAgg):
    def __init__(self, master=None):
        self.fig = matplotlib.figure.Figure((9,6))
        super().__init__(self.fig, master=master)
        self.ax = self.fig.add_subplot(111)

    def plot(self, row=0, column=0, data=[], labels=[], title="Grafico Circular"):

        self.get_tk_widget().grid(
            row=row, 
            column=column, 
            sticky=tk.NSEW
        )

        self.ax.clear()

        patches, texts, autotexts = self.ax.pie(data, labels=labels, autopct='%1.1f%%') 

        for text in texts:
            label = text.get_text().split(':')[0]
            label_size = len(label)
            if label_size > 10:
                new_font_size = 10 - (label_size/10)
                text.set_fontsize(new_font_size)

        self.ax.set_title(title)

        self.draw()