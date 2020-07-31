import time

def timestamp(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print(f'Process taked {round(end - start)} seconds.')
    return wrapper