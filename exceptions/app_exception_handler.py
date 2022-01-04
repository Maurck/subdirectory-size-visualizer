

def exception_to_info_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            args[0].info_box.write(e)
    return inner_function
    