from gui.gui import GUI
from gui.app_button import AppButton
from gui.app_directory_pie_canvas import AppDirectoryPieCanvas
from gui.app_entry import AppEntry
from gui.app_frame import AppFrame
from gui.app_info_box import AppInfoBox
from gui.app_label import AppLabel
from exceptions.app_exception_handler import exception_to_info_handler

class AppGUI(GUI):
    def __init__(self, title="Aplicación", dimensions="1400x600", default_folder_path = r'C:\Program Files (x86)', current_min_size_mb=500):
        super().__init__(title=title, dimensions=dimensions)
        
        self.set_variables(default_folder_path, current_min_size_mb)

        # Elementos: Pie, opciones
        self.create_elements_frame()

        # Pie
        self.create_pie_frame()
        self.create_directory_pie_canvas()

        # Opciones
        self.create_options_frame()
        self.create_options_elements()

        # Info
        self.create_info_frame()
        self.create_info_elements()


    def set_variables(self, default_folder_path, current_min_size_mb):
        self.default_folder_path = default_folder_path
        self.current_folder_path = self.default_folder_path
        self.previous_folder_path = []
        self.current_min_size_mb = current_min_size_mb

    def create_pie_frame(self):
        self.pie_frame = AppFrame(self.window, 0, 0)

    def create_directory_pie_canvas(self):
        self.directory_pie_canvas = AppDirectoryPieCanvas(self.pie_frame, 0, 0)

    def create_elements_frame(self):
        self.elements_frame = AppFrame(self.window, 0, 1)

    def create_options_frame(self):
        self.options_frame = AppFrame(self.elements_frame, 0, 0)

    def create_options_elements(self): 
        # Next Directory Label
        self.next_directory_label = AppLabel(self.options_frame, 0, 0, 'Ingrese siguiente carpeta:', width=25)

        # Next Directory Entry
        self.next_directory_entry = AppEntry(self.options_frame, 0, 1, '', width=20)

        # Next Directory button
        self.next_directory_button = AppButton(self.options_frame, 0, 2, 'Ir', lambda: self.next_pie(), padx=30)

        # Return button
        self.return_button = AppButton(self.options_frame, 1, 1, 'Volver', lambda: self.return_pie())

        # Filter label
        self.filter_label = AppLabel(self.options_frame, 2, 0, 'Tamaño minimo a filtrar (MB): ', width=25)

        # Filter Entry
        self.filter_entry = AppEntry(self.options_frame, 2, 1)

        # Actualize Button
        self.actualize_button = AppButton(self.options_frame, 2, 2, 'Actualizar', lambda: self.actualize_pie(self.filter_entry.get()))

        # Jump to directory Label
        self.jump_label = AppLabel(self.options_frame, 3, 0, 'Saltar a directorio: ', width=25)

        # Jump Entry
        self.jump_entry = AppEntry(self.options_frame, 3, 1, width=20)

        # Jump Button 
        self.jump_button = AppButton(self.options_frame, 3, 2, 'Saltar', lambda: self.jump_to_directory(self.jump_entry.get()))

    def create_info_frame(self):
        self.info_frame = AppFrame(self.elements_frame, 1, 0)

    def create_info_elements(self):
        # Info Label
        self.info_label = AppLabel(self.info_frame, 0, 0, 'Logs: ', width=25, pady=10)

        # Info Text
        self.info_box = AppInfoBox(self.info_frame, 1, 0, width=50, height=14)

    # Refactorizar

    def set_current_folder_path(self, folder_path):
        self.current_folder_path = folder_path

    def set_previous_folder_path(self):
        self.previous_folder_path.append(self.current_folder_path)

    @exception_to_info_handler
    def next_pie(self):
        if self.next_directory_entry.get() == '':
            raise Exception('Ingrese una ruta')
        try:
            next_folder_path = f'{self.current_folder_path}\{self.next_directory_entry.get()}'
            self.directory_pie_canvas.plot(folder_path=next_folder_path, min_size_mb=self.current_min_size_mb)
            self.set_previous_folder_path()
            self.set_current_folder_path(next_folder_path)
        except:
            raise Exception(f'La carpeta "{self.next_directory_entry.get()}" no forma parte del subdirectorio actual')

    @exception_to_info_handler
    def return_pie(self):
        if len(self.previous_folder_path) > 0:
            next_folder_path = self.previous_folder_path.pop()
            self.directory_pie_canvas.plot(folder_path=next_folder_path, min_size_mb=self.current_min_size_mb)
            self.set_current_folder_path(next_folder_path)
        else:
            raise Exception('No hay carpetas anteriores')

    @exception_to_info_handler
    def actualize_pie(self, min_size_mb):

        try:
            integer_min_size_mb = int(min_size_mb)
        except:
            raise Exception('El tamaño en MB debe ser un numero')

        if int(integer_min_size_mb) < 0:
            raise Exception('El tamaño en MB debe ser positivo')

        self.current_min_size_mb=int(min_size_mb)
        self.directory_pie_canvas.plot(folder_path=self.current_folder_path, min_size_mb=self.current_min_size_mb)

    @exception_to_info_handler
    def jump_to_directory(self, folder_path):

        if self.jump_entry.get() == '':
            raise Exception('Ingrese una ruta')

        try:
            self.directory_pie_canvas.plot(folder_path=folder_path, min_size_mb=self.current_min_size_mb)

            self.set_previous_folder_path()
            self.current_folder_path=folder_path
        except:
            raise Exception(f'La ruta "{self.jump_entry.get()}" no es válida')
