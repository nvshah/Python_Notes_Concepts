
# Expression to remove all files in current directory
exp = "__import__('subprocess').getoutput('rm –rf *')" 

#! WARNING dOn't run this {exp} it will remove all file inn current dir 
#eval(exp) 