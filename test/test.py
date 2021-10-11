from tkinter import * 

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
  
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot_pie(window):

    # folder_path = 'C:/'
    # folder_size = '22 GB'
    directory_sizes = [6801084416, 6710886400, 34493015128, 39464709305, 14879053450, 75300780277, 27240219338, 606999755]
    names = ['hiberfil.sys: 6.33 GB', 'pagefile.sys: 6.25 GB', 'Program Files: 32.12 GB', 'Program Files (x86): 36.75 GB', 'ProgramData: 13.86 GB', 'Users: 70.13 GB', 'Windows: 25.37 GB', 'Otros: 578.88 MB']

    fig = matplotlib.figure.Figure(figsize=(7,4))
    ax = fig.add_subplot(111)
    ax.pie(directory_sizes, labels=names) 

    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
window = Tk()
  
# setting the title 
window.title('Test')
  
# dimensions of the main window
window.geometry("800x600")
  
# button that displays the plot
plot_button = Button(master = window, 
                     command = lambda: plot_pie(window),
                     height = 2, 
                     width = 15,
                     text = "Generar Grafico")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()