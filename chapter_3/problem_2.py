import os

def extcount(directory):
    ext_dir = {}
    walk = os.walk(directory)
    for files in walk.next()[2]:
        ext = files.split('.')[1]
        ext_dir[ext] = ext_dir.get(ext,0) + 1
    return ext_dir


a = extcount('/home/dheeraj/repos/anand_python')
for (key, value) in a.items():
    print key + '  ---->  ' + str(value)
