def mutate(string):
    final_list = [string]
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(0, len(alphabets)):

        for j in range(0, len(string)+1):
            final_list.append(string[:j] + alphabets[i] + string[j:])
            final_list.append(string[:j] + alphabets[i] + string[j + 1:])

    for index in range(0, len(string)):
        final_list.append(string[:index] + string[index+1:])

        if index < len(string)-1:
            a,b = string[index + 1], string[index]
            final_list.append(string[:index] + a + b + string[index + 2:])

    return set(final_list)

print mutate('jython')
