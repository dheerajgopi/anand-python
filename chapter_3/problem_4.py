import os

rootdir = '/home/dheeraj/Pictures'

for dirname, subdir, files in os.walk(rootdir):
    for fname in files:
        print ('\t%s' %subdir)
        print ('\t\t%s' %fname)
