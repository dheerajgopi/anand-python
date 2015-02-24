import os

def pyfiles(directory):
    walk = os.walk(directory)
    for dirname, subdir, files in walk:
        for filename in files:
            if filename.split('.')[-1] == 'py':
                yield dirname + '/' + filename

def pyread(pyfile):
    f = open(pyfile)
    lines = 0
    for line in f:
        lines += 1
    return lines

a = pyfiles('/home/dheeraj/repos/think-python')

total_lines = 0

for i in a:
    total_lines += pyread(i)
print '\nTotal lines of python code :- ', total_lines, '\n'
