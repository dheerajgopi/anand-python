def array(list_num, list_length):

    array_list = []

    for i in range(0, list_num):
        array_element = []

        for j in range(0, list_length):
            array_element.append(None)

        array_list.append(array_element)

    return array_list

a = array(3,4)
print a
