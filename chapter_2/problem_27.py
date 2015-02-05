def triplets(num):
    return [(i, j, i+j) for i in range(1, num) for j in range(1, num) if i + j < num and i <= j]

print triplets(9)
