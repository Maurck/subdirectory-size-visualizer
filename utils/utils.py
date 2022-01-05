import os
import concurrent.futures
from itertools import repeat

def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f} {unit}{suffix}"
        b /= factor
    return f"{b:.2f} Y{suffix}"

def get_directory_data(directory, min_size_mb):
    directory_size = get_directory_size(directory)
    directory_name = os.path.basename(directory) + ": " + get_size_format(directory_size)

    if directory_size <= 0:
        return

    if directory_size / (1024.0 * 1024.0) < min_size_mb:
        return (directory_size, directory_name, False)   

    return (directory_size, directory_name, True)

def get_directories_data(folder_path=r'C:\Program Files (x86)', min_size_mb=500):

    others_size = 0
    directory_sizes = []
    directory_names = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        listdir = os.listdir(folder_path)
        directories = [os.path.join(folder_path, directory) for directory in listdir]
        results = executor.map(get_directory_data, directories, repeat(min_size_mb))
    
    results_list = [result for result in results if result is not None]

    directory_sizes = [result[0] for result in results_list if result[2] is True]
    directory_names = [result[1] for result in results_list if result[2] is True]

    #Others
    others_size = sum([result[0] for result in results_list if result[2] is False])
    directory_sizes.append(others_size)
    directory_names.append("Otros: " + get_size_format(others_size))

    return (directory_sizes, directory_names)
