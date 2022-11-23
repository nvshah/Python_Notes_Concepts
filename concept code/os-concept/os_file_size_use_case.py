import time 
import os 
from heapq import nlargest

def walk_files_and_sizes(start_at:str):
    for root, direc, files in os.walk(start_at):
        for f in files:
            file_path = os.path.join(root, f)
            try:
                size = os.path.getsize(file_path)
                yield file_path, size
            except OSError:
                # In case file do not allow permission
                print('Something went wrong')
                yield file_path, -1

def find_largest_file(start_at: str, n: int):
    largest = nlargest(n, walk_files_and_sizes(start_at), key=lambda x: x[1])
    MB = 1024 * 1024
    for path, size in largest:
        print(f'Size : {size//MB} MB, - Path : {path}')

if __name__ == '__main__':
    start = time.perf_counter()
    find_largest_file("/Users/nipunshah/Documents/Words/", 2)
    elapsed = time.perf_counter() - start 
    print('Elapsed time :- ', elapsed, " Seconds")