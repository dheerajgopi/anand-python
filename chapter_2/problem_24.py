def zip(a,b):
    return [(a[i],b[i]) for i in range(0,min(len(a),len(b)))]

print zip(['a','b'],[1,2,3,4,5])
