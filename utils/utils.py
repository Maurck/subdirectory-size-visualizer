import os

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

def get_directories_data(folder_path=r'C:\Program Files (x86)', min_size_mb=500):

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
        
        #print(f"{os.path.basename(directory)} : {get_size_format(directory_size)}")
        directory_sizes.append(directory_size)
        names.append(os.path.basename(directory) + ": " + get_size_format(directory_size))

    directory_sizes.append(others_size)
    names.append("Otros: " + get_size_format(others_size))

    return (directory_sizes, names)