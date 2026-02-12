def my_filter_with_sort(my_list, filter_value, reverse=False):
    new_list = []
    for elem in my_list:
        if elem.variable_a == filter_value:
            new_list.append(elem)
    new_list.sort(key=lambda x : x.variable_b, reverse=reverse)
    return new_list