def sqr(x):
    return x*x

def vectorize(fun):
    def g(lst):
        res = []
        for elem in lst:
            v = fun(elem)
            res.append(v)
        return res
    return g

a = vectorize(sqr)
print a([1,2,3])
