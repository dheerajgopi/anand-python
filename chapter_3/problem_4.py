import os

rootdir = '/home/dheeraj/Pictures'

walk = os.walk(rootdir)

for dirname, subdir, files in walk:
    print '\n' + dirname
    for file_name in files:
        print '-- --' + file_name
        for dir_name in subdir:
            print '-- --' + dir_name
