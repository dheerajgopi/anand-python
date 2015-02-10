import textwrap

def wrap(file_name, width = 70):

    wrapped_text = []
    f = open(file_name)

    for line in f:
        text = line.strip()
        wrapped_text += textwrap.wrap(text, width)

    return wrapped_text

a = wrap('she.txt', 30)

for line in a:
    print line
