import os

os.chdir('/Users/nipunshah/Documents/Python/concept code/os-concept/demo_files')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    *f_rest, f_num =  file_name.split('-')

    f_rest = ''.join([r.strip() for r in f_rest])
    # zfill so that 1 & 10 are not next to each others
    f_num = f_num.strip()[1:].zfill(2)  # get rid of #

    new_name = f'{f_num}-{f_rest}{file_ext}'

    os.rename(f, new_name)

