def grep(file_name, string): 

    f = open(file_name)

    line_with_string = []

    for line in f:
        if string in line.strip():
            line_with_string.append(line.strip())
    return line_with_string

a = grep('she.txt','sure')

for line in a:
    print line
