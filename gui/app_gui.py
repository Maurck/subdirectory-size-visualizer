import tkinter as tk
from tkinter import * 

from gui.gui import GUI
from gui.pie.directory_pie_canvas import DirectoryPieCanvas

class AppGUI(GUI):
    def __init__(self, title="Aplicación", dimensions="1300x600", default_folder_path = r'C:\Program Files (x86)', current_min_size_mb=500):
        super().__init__(title=title, dimensions=dimensions)
        
        self.set_variables(default_folder_path, current_min_size_mb)

        self.create_pie_canvas()
        self.create_elements_frame()
        self.create_options_frame()
        self.create_info_frame()
        self.create_elements()


    def set_variables(self, default_folder_path, current_min_size_mb):
        self.default_folder_path = default_folder_path
        self.current_folder_path = self.default_folder_path
        self.previous_folder_path = []
        self.previous_folder_path.append(self.current_folder_path)
        self.current_min_size_mb = current_min_size_mb

    def create_elements_frame(self):
        self.elements_frame = Frame(self.window)
        self.elements_frame.grid(row=0, column=1, sticky=tk.N)

    def create_options_frame(self):
        self.options_frame = Frame(self.elements_frame)
        self.options_frame.grid(row=0, column=0, sticky=tk.N)

    def create_info_frame(self):
        self.info_frame = Frame(self.elements_frame)
        self.info_frame.grid(row=1, column=0, sticky=tk.N)

    def create_pie_canvas(self):
        #pie frame
        self.pie_frame = Frame(self.window)
        self.pie_frame.grid(row=0, column=0)
        #directory canvas
        self.directory_pie_canvas = self.create_directory_pie_canvas(
            self.pie_frame,
            row=0,
            column=0, 
            folder_path=r'C:\Program Files (x86)', 
            min_size_mb=500
        )

    def create_elements(self):
        
        # Next Directory Label
        self.next_directory_label = self.create_label(
            master=self.options_frame,
            text=f'Ingrese Siguiente Directorio:',
            width=25,
            row=0, 
            column=0,
        )

        # Next Directory Entry
        self.next_directory_entry = self.create_entry(
            master=self.options_frame,
            text=f'', 
            width=20,
            row=0, 
            column=1
        )

        # Next Directory button
        self.next_directory_button = self.create_button(
            lambda: self.next_pie(),
            name="Ir",
            master=self.options_frame,
            row=0,
            column=2,
            padx=30
        )

        # Return button
        self.return_button = self.create_button(
            lambda: self.return_pie(),
            name="Volver",
            row=1,
            column=1,
            master=self.options_frame
        )

        # Filter label
        self.filter_label = self.create_label(
            text="Tamaño minimo a filtrar (MB): ",
            width=25,
            row=2,
            column=0,
            master=self.options_frame
        )
        # Filter Entry
        self.filter_entry = self.create_entry(
            text='',
            master=self.options_frame,
            row=2,
            column=1
        )
        # Actualize 
        self.actualize_button = self.create_button(
            lambda: self.actualize_pie(self.filter_entry.get()),
            name="Actualizar",
            master=self.options_frame,
            row=2, 
            column=2
        )
        # Jump to directory
        self.jump_label = self.create_label(
            text="Saltar a directorio: ",
            width=25,
            row=3,
            column=0,
            master=self.options_frame
        )
        # Jump Entry
        self.jump_entry = self.create_entry(
            text='',
            master=self.options_frame,
            row=3,
            width=20,
            column=1
        )
        # Actualize 
        self.jump_button = self.create_button(
            lambda: self.jump_to_directory(self.jump_entry.get()),
            name="Saltar",
            master=self.options_frame,
            row=3, 
            column=2
        )

        # Info Label
        self.info_label = self.create_label(
            text="Logs: ",
            width=25,
            row=0,
            column=0,
            pady=10,
            master=self.info_frame
        )
        # Info Text
        self.info_text = self.create_text(
            master=self.info_frame,
            width=50,
            height=14,
            row=1,
            column=0
        )

    def create_directory_pie_canvas(self, master, row=0, column=0, folder_path=r'C:\Program Files (x86)', min_size_mb=500):

        directory_pie_canvas = DirectoryPieCanvas(
            master = master
        )

        directory_pie_canvas.plot(row=row, column=column, min_size_mb=min_size_mb, folder_path=folder_path)

        return directory_pie_canvas


    def exception_to_info_handler(func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                args[0].write_info(e)
        return inner_function

    def set_current_folder_path(self, folder_path):
        self.current_folder_path = folder_path

    def set_previous_folder_path(self):
        self.previous_folder_path.append(self.current_folder_path)

    @exception_to_info_handler
    def jump_to_directory(self, folder_path):
        self.set_previous_folder_path()
        self.current_folder_path=folder_path
        
        self.directory_pie_canvas.plot(folder_path=folder_path, min_size_mb=self.current_min_size_mb)

    @exception_to_info_handler
    def actualize_pie(self, min_size_mb):
        if int(min_size_mb) < 0:
            raise Exception('El tamaño en MB debe ser positivo')
        
        self.current_min_size_mb=int(min_size_mb)
        self.directory_pie_canvas.plot(folder_path=self.current_folder_path, min_size_mb=self.current_min_size_mb)

    @exception_to_info_handler
    def return_pie(self):
        if len(self.previous_folder_path) > 0:
            next_folder_path = self.previous_folder_path.pop()
            self.directory_pie_canvas.plot(folder_path=next_folder_path, min_size_mb=self.current_min_size_mb)
            self.set_current_folder_path(next_folder_path)

    @exception_to_info_handler
    def next_pie(self):
        if self.next_directory_entry.get() == '':
            raise Exception('Ingrese una ruta')

        next_folder_path = f'{self.current_folder_path}\{self.next_directory_entry.get()}'
        self.directory_pie_canvas.plot(folder_path=next_folder_path, min_size_mb=self.current_min_size_mb)
        self.set_previous_folder_path()
        self.set_current_folder_path(next_folder_path)

    def write_info(self, text):
        self.info_text.configure(state='normal')
        self.info_text.delete('1.0', END)
        self.info_text.insert(INSERT, text)
        self.info_text.configure(state='disabled')
