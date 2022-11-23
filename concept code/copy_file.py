import os
from shutil import copyfile

openfile = input('Enter the input file name:')
outputfile = input('Enter the output file name:')

copyfile(openfile, outputfile)