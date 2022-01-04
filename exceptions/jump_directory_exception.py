from ..gui.app_gui import AppGUI

class NextPie:
    def __init__(self, appGUI : AppGUI):
        self.appGUI = appGUI

    def __enter__(self):
        if self.appGUI.next_directory_entry.get() == '':
            raise Exception('Ingrese una ruta')

        next_folder_path = f'{self.current_folder_path}\{self.next_directory_entry.get()}'
        self.appGUI.directory_pie_canvas.plot(folder_path=next_folder_path, min_size_mb=self.current_min_size_mb)
        self.appGUI.set_previous_folder_path()
        self.appGUI.set_current_folder_path(next_folder_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichero:
            self.fichero.close()

