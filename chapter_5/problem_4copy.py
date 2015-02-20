import os

def pycount(directory):
    walk = os.walk(directory)
    for files in walk.next()[2]:
        ext = files.split('.')[1]
        if ext == 'py':
            yield 1
        else:
            yield 0


a = pycount('/home/dheeraj/repos/anand_python')
total = 0

for i in a:
    total += i
print total
