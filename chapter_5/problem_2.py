def readfiles(file_name):
    for line in open(file_name):
        yield line

def chars_40(line):
    l = line.strip()
    if len(l) > 40:
        return line

def showgrep(pattern, *files):
    for file_name in files:
        for line in readfiles(file_name):
            l = chars_40(line)
            if l != None:
                yield l


a = showgrep('abcd', 'abcd.txt', 'efgh.txt')

for i in a:
    print i
