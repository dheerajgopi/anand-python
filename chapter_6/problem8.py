def count_change(amount, ways):

    if amount < 0 or len(ways) == 0:
        return 0

    if amount == 0:
        return 1

    n = ways[0]
    return count_change(amount, ways[1:]) + count_change(amount - n, ways)

print count_change(100,[1,5,10,25,50])
