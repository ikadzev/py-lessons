def cycle(lst, num):
    i = 0
    while num != 0:
        if i > len(lst) - 1:
            i = 0
        yield lst[i]
        i += 1
        num -= 1


print(list(cycle([1, 2, 3], 10)))
