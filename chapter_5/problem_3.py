import os
def findfile(path):
    rootdir = path
    walk = os.walk(rootdir)

    for dirname, subdir, files in walk:
        for file_name in files:
            yield dirname + '/' + file_name

a = findfile('/home/dheeraj/Pictures')

for i in a:
    print i
