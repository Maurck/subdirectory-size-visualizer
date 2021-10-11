
from directory import Directory
from tkinter import * 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.figure

class GUI:
    def __init__(self, title="Aplicación", dimensions="1200x600", default_folder_path = r'C:\Program Files (x86)'):

        self.default_folder_path = default_folder_path
        self.current_folder_path = self.default_folder_path
        self.previous_folder_path = []
        self.previous_folder_path.append(self.current_folder_path)

        self.directory = Directory()

        self.create_window(title=title, dimensions=dimensions)
        self.create_initial_elements()

    def create_window(self, title, dimensions):

        self.window = Tk()
        self.window.title(title)
        self.window.geometry(dimensions)

    def create_initial_elements(self):

        self.create_pie()

        self.current_directory_label = self.create_label(
            text=f'Directorio actual: {self.default_folder_path}', 
            height=2, 
            width=55,
            row=6, 
            column=1 
        )

        self.actualize_button = self.create_button(
            func=self.actualize_pie,
            name='Actualizar',
            height=2,
            width=55,
            row=7,
            column=1
        )

        self.return_button = self.create_button(
            func=self.return_pie,
            name='Volver',
            height=2,
            width=55,
            row=9,
            column=1
        )

        self.next_directory_label = self.create_label(
            text='Siguiente Directorio:', 
            height=2, 
            width=55,
            row=12, 
            column=1 
        )

        self.next_directory_entry = self.create_entry(
            text='', 
            width=55,
            row=13, 
            column=1 
        )

        self.next_directory_button = self.create_button(
            func=self.next_pie,
            name='Ir',
            height=2,
            width=55,
            row=14,
            column=1
        )

    def create_pie(self):

        self.pie_fig = matplotlib.figure.Figure(figsize=(8, 6))
        self.pie_canvas = FigureCanvasTkAgg(self.pie_fig, master = self.window) 
        self.pie_ax = self.pie_fig.add_subplot(111)

        self.directory.plot_pie_in_gui(gui=self, folder_path=self.default_folder_path, min_size_mb=100)

    def create_label(self, text='label', height=2, width=15, row=0, column=1):
        label = Label(
            master = self.window,
            height = height, 
            width = width,
            text = text
        )

        label.grid(row=row, column=column)
        return label

    def create_entry(self, text='', width=15, row=0, column=1):
        entry = Entry(
            master = self.window,
            width = width,
            text = text
        )

        entry.grid(row=row, column=column)
        return entry

    def create_button(self, func, name, height=2, width=15, row=0, column=1):

        button = Button(
            master = self.window, 
            command = func,
            height = height, 
            width = width,
            text = name
        )
        
        button.grid(row=row, column=column)
        return button

    def run_gui(self):

        self.window.mainloop()
    
    def plot_pie(self, data, labels, title="Gráfico Circular", row=0, column=0, rowspan=24):

        self.pie_canvas.get_tk_widget().grid(
            row=row, 
            column=column, 
            rowspan=rowspan
        )

        self.pie_ax.clear()
        self.pie_ax.pie(data, labels=labels) 
        self.pie_ax.set_title(title)

        self.pie_canvas.draw()

    def set_current_folder_path(self, folder_path):
        self.current_folder_path = folder_path

    def set_previous_folder_path(self):
        self.previous_folder_path.append(self.current_folder_path)

    def actualize_pie(self):
        self.directory.plot_pie_in_gui(gui=self, folder_path=self.current_folder_path, min_size_mb=100)

    def return_pie(self):
        try:
            next_folder_path = self.previous_folder_path.pop()
            self.directory.plot_pie_in_gui(gui=self, folder_path=next_folder_path, min_size_mb=100)
            self.set_current_folder_path(next_folder_path)
        except IndexError:
            pass

    def next_pie(self):
        next_folder_path = f'{self.current_folder_path}/{self.next_directory_entry.get()}'
        self.directory.plot_pie_in_gui(gui=self, folder_path=next_folder_path, min_size_mb=100)
        self.set_previous_folder_path()
        self.set_current_folder_path(next_folder_path)
    