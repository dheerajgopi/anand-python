# the return values of key functions are checked instead of the original list
def unique(a_list, key = lambda x: x):

    unique_elements = []
    temp_list = [key(i) for i in a_list]

    for i in range(0,len(temp_list)):
        if temp_list[i] not in temp_list[i+1:]:
            unique_elements.append(temp_list[i])

    return unique_elements

print unique(['python', 'Java', 'PYTHON', 'jAVA', 'perl'], key = lambda x: x.lower())
