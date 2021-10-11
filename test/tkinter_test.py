import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

folder_path = 'C:/'
folder_size = '22 GB'
directory_sizes = [6801084416, 6710886400, 34493015128, 39464709305, 14879053450, 75300780277, 27240219338, 606999755]
names = ['hiberfil.sys: 6.33 GB', 'pagefile.sys: 6.25 GB', 'Program Files: 32.12 GB', 'Program Files (x86): 36.75 GB', 'ProgramData: 13.86 GB', 'Users: 70.13 GB', 'Windows: 25.37 GB', 'Otros: 578.88 MB']

fig = matplotlib.figure.Figure(figsize=(8,5))
ax = fig.add_subplot(111)
ax.pie(directory_sizes, labels=names) 

window= tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
canvas.draw()

window.mainloop()