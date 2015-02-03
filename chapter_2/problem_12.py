def group(a, size):

    grouped_list = []

    for i in range(0, len(a), size):
        grp = a[i:i+3]
        grouped_list.append(grp)

    return grouped_list

print group([1,2,3,4,5,6,7,8,9,10],3)
