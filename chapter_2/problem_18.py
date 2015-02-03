# printing each line in reverse order
file_name = open('she.txt')
rev_file = [line.strip() for line in file_name]

for line in rev_file:
    words = line.split(' ')
    print ' '.join(words[::-1])
