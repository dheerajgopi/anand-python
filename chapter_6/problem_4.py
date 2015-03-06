def treemap(fun, lst):
    map_list = []
    for elem in lst:
        if isinstance(elem, list):
            map_list.append(treemap(fun,elem))
        else:
            map_list.append(fun(elem))
    return map_list



a = [1,2,[3,[2,7], 4]]
print a
print treemap(lambda x:x*x, a)
b = [1,2,[3,4],5]
print b
print treemap(lambda x:x*x, b)
