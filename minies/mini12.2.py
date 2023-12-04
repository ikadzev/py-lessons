def chain(*lists):
    for lst in lists:
        yield from lst


my_list = [42, 13, 7]
print(list(chain([1, 2, 3], ['a', 'b'], my_list)))
