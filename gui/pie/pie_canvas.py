import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.figure

class PieCanvas(FigureCanvasTkAgg):
    def __init__(self, master=None):
        self.fig = matplotlib.figure.Figure((8,6))
        super().__init__(self.fig, master=master)
        self.ax = self.fig.add_subplot(111)

    def plot(self, row=0, column=0, data=[], labels=[], title="Grafico Circular"):

        self.get_tk_widget().grid(
            row=row, 
            column=column, 
            sticky=tk.NSEW
        )

        self.ax.clear()
        self.ax.pie(data, labels=labels) 
        self.ax.set_title(title)

        self.draw()