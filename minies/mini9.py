def format_table(list1, list2, list3):
    length = 11
    for str in list2:
        length += len(str) + 3
    maxx = max([len(i) for i in list1])

    print(f'| {"Benchmark":<{max(9, maxx)}} |', end = '')
    for i in range(len(list2)):
        print(f' {list2[i]} |', end='')
    
    print('\n|' + '-' * (length + max(0, maxx-9)) + '|')
    for i in range(len(list1)):
        print(f'| {list1[i]:<{max(9, maxx)}} | ', end='')
        for j in range(len(list3[i])):
            print(f'{list3[i][j]:<{len(list2[j])}} | ', end='')
        print()
    


format_table(["best case", "worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.5345345345346, 2.00], [3.3, 2.9, 3.9]])