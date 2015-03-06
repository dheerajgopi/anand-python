def treereverse(lst):
    res = []
    for elem in lst:
        if isinstance(elem, list):
            res.append(treereverse(elem))
        else:
            res.append(elem)
    lst.reverse()
    return lst

a = [1,[1,2,[9,8]],3]
print a
print treereverse(a)
