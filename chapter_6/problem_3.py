def unflatten_dict(d):
    result = {}
    for key, value in d.items():
        key_parts = key.split(".")
        rdict = result
        for part in key_parts[:-1]:
            if part not in rdict:
                rdict[part] = {}
            rdict = rdict[part]
        rdict[key_parts[-1]] = value
    return result


a= {'a':1, 'c.x':2, 'c.y.u':3, 'c.y.v':4, 'b':5}
print unflatten_dict(a)
