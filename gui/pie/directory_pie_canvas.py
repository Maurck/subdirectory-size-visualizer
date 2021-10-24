from gui.pie.pie_canvas import PieCanvas
from utils.utils import get_directories_data


class DirectoryPieCanvas(PieCanvas):
    def __init__(self,master=None):
        super().__init__(master=master)

    def plot(self, row=0, column=0, folder_path=r'C:\Program Files (x86)', min_size_mb=500):
        data, labels = get_directories_data(folder_path, min_size_mb)
        super().plot(row=row, column=column, title=f'Directorio: {folder_path} | Filtro: {min_size_mb} MB', data=data, labels=labels)