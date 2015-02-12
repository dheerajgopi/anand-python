def product(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0

    else:
        return n1 + product(n1, n2-1)


print product(0,1)
print product(1,0)
print product(2,1)
print product(9,9)


