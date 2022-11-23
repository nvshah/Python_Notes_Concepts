import os 
import shutil

print(os.getcwd())  # /Users/nipunshah/Documents/Python/concept code

os.chdir('/Users/nipunshah/Documents/Python')

# Note still my python command runs from `concept code` dir but my curr working dir is changed
#print(os.getcwd()) # /Users/nipunshah/Documents/Python

#print(os.listdir())  # list files & folders in cwd()

print(os.walk(os.getcwd()))

print(os.environ.get("HOME"))

shutil.rmtree() # To remove non-empty directory
os.rmdir()  # to remove empty directory

