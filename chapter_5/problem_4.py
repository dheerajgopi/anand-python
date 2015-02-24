import os

def pycount(directory):
    walk = os.walk(directory)
    for dirname, subdir, files in walk:
        for filename in files:
            if filename.split('.')[-1] == 'py':
                yield 1

a = pycount('/home/dheeraj/repos/think-python')
total = 0

for i in a:
    total += i
print '\nTotal number of python files :-  ', total, '\n'
