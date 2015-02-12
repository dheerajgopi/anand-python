def flatten_dict(d, result = None, k = None):
    if result == None:
        result = {}

    if k == None:
        k = []

    for key in d:
        k.append(key)

        if isinstance(d[key], dict):
            flatten_dict(d[key], result, k)

        else:
            new_key = '.'.join(k)
            result[new_key] = d[key]

            if len(k) > 1:
                del k[-1]

            else:
                k = []

    return result

a = {'a':1, 'b':{'x':2, 'y':{'u':4, 'v':5}}, 'c':6}

print flatten_dict(a)
