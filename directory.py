import os

from utils.utils import get_size_format
from utils.utils import get_directory_size

class Directory:
    def __init__(self):
        pass

    def get_directories_data(self, folder_path='C:/', min_size_mb=500):

        others_size = 0
        directory_sizes = []
        names = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)

            if directory_size <= 0:
                continue

            if directory_size / (1024.0 * 1024.0) < min_size_mb:
                others_size+=directory_size
                continue
            
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory) + ": " + get_size_format(directory_size))

        directory_sizes.append(others_size)
        names.append("Otros: " + get_size_format(others_size))

        return (directory_sizes, names)

    def plot_pie_in_gui(self, gui, folder_path='C:/', min_size_mb=500, row=0, column=0):

        data, labels = self.get_directories_data(folder_path, min_size_mb)
        # create pie plot
        gui.plot_pie(data, labels, title=f'Directorio: {folder_path}', row=row, column=column)
