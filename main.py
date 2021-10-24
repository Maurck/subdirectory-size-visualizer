from gui.app_gui import AppGUI

if __name__ == '__main__':

    folder_path = r'C:\Program Files (x86)'
    app = AppGUI(title="Visualizador de tamaños de carpetas", default_folder_path=folder_path)
    
    app.run_gui()
