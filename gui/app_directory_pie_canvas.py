from gui.pie.directory_pie_canvas import DirectoryPieCanvas

class AppDirectoryPieCanvas(DirectoryPieCanvas):

    def __init__(self, master, row=0, column=0, folder_path=r'C:\Program Files (x86)', min_size_mb=500):
        super().__init__(master = master)
        self.plot(row=row, column=column, min_size_mb=min_size_mb, folder_path=folder_path)
