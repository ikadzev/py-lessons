def flatten(lst, depth=None):
    ret_list = []
    for x in lst:
        if isinstance(x, list) and depth != 0:
            ret_list.extend(flatten(x, depth - 1 if depth else None))
        else:
            ret_list.append(x)
    return ret_list

print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))