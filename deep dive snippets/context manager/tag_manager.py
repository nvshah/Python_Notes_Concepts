class Tag:
    def __init__(self, tagname):
        self._tagname = tagname 
    
    def __enter__(self):
        print(f'<{self._tagname}> ', end="")
    
    def __exit__(self, ex_type, ex_val, ex_tb):
        print(f'</{self._tagname}> ', end="")

if __name__ == '__main__':
    with Tag('title'):
        print('Hello', end=' ')
        with Tag('b'):
            print('World', end= ' ')