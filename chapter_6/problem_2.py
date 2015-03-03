def flatten_dict(d):
    flat_dict = {}

    def _flatten_dict(d, k = []):
        for key, val in d.items():

            if isinstance(val, dict):
                _flatten_dict(val, k + [key])

            else:
                new_key = '.'.join(k + [key])
                flat_dict[new_key] = val
    _flatten_dict(d)
    return flat_dict

a = {'a':1, 'c':{'x':2, 'y':{'u':4, 'v':5}}, 'b':6}

print flatten_dict(a)
