def wrap(text, width = 70):
    text_list = list(text)
    wrap_list = []
    for i in range(width, len(text_list)+width+1, width):
        wrap_list += [text[i:i+width]]
    return wrap_list

f=open('she.txt')
wrapped_text = []
for line in f:
    txt = line.strip()
    wrapped_text += wrap(txt,30)
    print wrapped_text    
for i in wrapped_text:
    print i
