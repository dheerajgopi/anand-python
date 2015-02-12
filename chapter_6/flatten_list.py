def flatten_list(lst, result = None):

    if result == None:
        result = []

    for i in lst:

        if isinstance(i, list):
            flatten_list(i, result)

        else:
            result.append(i)

    return result

a = [1,2,[3,[4,5],6],[7,8],9]

print flatten_list(a)
