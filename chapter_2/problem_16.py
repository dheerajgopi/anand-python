# sorting by extension
def extsort(file_list):

    temp_list = sorted([i.split('.') for i in file_list], key = lambda x: x[1])
    sorted_list = ['.'.join(i) for i in temp_list]

    return sorted_list

print extsort(['a.a','b.c','c.b'])
