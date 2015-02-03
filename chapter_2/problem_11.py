# using loop
def dups(a):

    duplicate_elements = []

    for i in range(0,len(a)):
        if a[i] in a[i+1:] and a[i] not in duplicate_elements:
            duplicate_elements.append(a[i])
    return duplicate_elements

print dups([1,2,2,3,3,4,5,6,7,5,4,5,6,7,5,4,5,6,7,5,4,5,6,7,5,4,5,6,7,5])
