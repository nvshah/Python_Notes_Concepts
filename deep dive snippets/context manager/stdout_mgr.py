import sys 

class StdOutMgr:
    def __init__(self, filename):
        self.fname = filename 
        self.actual_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self.fname, 'w')
        sys.stdout = self._file

    def __exit__(self, err_type, err_val, err_tb):
        self._file.close()
        sys.stdout = self.actual_stdout

if __name__ == '__main__':
    fname = r'/Users/nipunshah/Documents/Python/deep dive snippets/context manager/test_stdout.txt'
    with StdOutMgr(fname):
        # print to file 
        print('Line 1')
        print('Linne 2')
    # print to console
    print('Line 1')
    print('Line 2')