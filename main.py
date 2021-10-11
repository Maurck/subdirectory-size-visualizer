from gui import GUI

if __name__ == '__main__':

    folder_path = r'C:\Program Files (x86)'
    gui = GUI(title="Visualizador de tamaños de carpetas", default_folder_path=folder_path)
    
    gui.run_gui()
