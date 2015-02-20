def readfiles(file_name):
    for line in open(file_name):
        yield line

def grep(pattern, line):
    if pattern in line:
        yield line

def printline(line):
    print line

def showgrep(pattern, files):
    for line in readfiles(files):
        if grep(pattern, line):
            printline(line)
print showgrep('abcd', 'abcd.txt')
