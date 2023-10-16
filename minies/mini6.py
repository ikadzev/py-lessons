def flatten(lst):
    ret_list = []
    for x in lst:
        if isinstance(x, list):
            ret_list.extend(flatten(x))
        else:
            ret_list.append(x)
    return ret_list

print(flatten([1, 2, [4, 5], [6, [7]], 8]))