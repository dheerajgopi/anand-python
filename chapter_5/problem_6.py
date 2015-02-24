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
        if not comment_or_empty(line) == True:
            lines += 1
    return lines

def comment_or_empty(line):
    if line.strip() == '' or line.startswith('#') == True:
        return True


a = pyfiles('/home/dheeraj/repos/think-python')

total_lines = 0

for i in a:
    total_lines += pyread(i)

print '\nTotal lines of python code :- ', total_lines, '\n'
