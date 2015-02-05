# parse the text with the delimiter specified
# will ignore comment lines and blank lines
def parse(file_name, delim, comment):

    f = open(file_name)
    return [line.strip() for line in f if not line.startswith(comment) and line.strip()]

print parse('parsetext.txt', ',', '#')
