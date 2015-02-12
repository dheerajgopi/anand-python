import os

def extcount(directory):
    ext_dir = {}
    walk = os.walk(directory)
    for files in walk.next()[2]:
        stat = os.stat(directory + '/' + files)
        ext_dir[files] = (stat[6], stat[8]) # check os.stat
    return ext_dir


a = extcount('/home/dheeraj/repos/anand_python')

print '\n'
print 'file\t\t\tsize\t\t\ttime'
print '----\t\t\t----\t\t\t----'
print '\n'

for (key, value) in a.items():
    print key + '\t\t\t' + str(value[0]) + '\t\t\t' + str(value[1])

print '\n'
