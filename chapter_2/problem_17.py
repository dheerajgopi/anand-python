file_name = open('she.txt')
rev_file = [line.strip() for line in file_name]

for line in rev_file[::-1]:
    print line
