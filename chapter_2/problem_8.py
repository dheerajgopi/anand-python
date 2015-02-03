def cumulative_sum(a_list):
    sum_of_elements = 0

    for i in a_list:
        sum_of_elements += i

    return sum_of_elements

print cumulative_sum([1,2,3,4])
