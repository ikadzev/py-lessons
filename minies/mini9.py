def format_table(list1, list2, list3):
    maxes = [max(9, max([len(i) for i in list1]))] # задаём максимум длин для первого столбца
    for n in range(len(list2)):
        maxes.append(max(len(list2[n]), max([len(str(list3[j][n])) for j in range(len(list3))])))
        # выше формула для вычисления максимума длин для каждого столбца
    print(f'| {"Benchmark":<{maxes[0]}} | ', end = '') 
    for i in range(len(list2)):
        print(f' {list2[i]:<{maxes[i+1]}} |', end='') # вывод первой строки
    
    print('\n|' + '-' * (sum(maxes) + 3 * len(list2) + 3) + '|') # вывод второй строки

    for i in range(len(list1)): # вывод остальных строк
        print(f'| {list1[i]:<{maxes[0]}} | ', end='')
        for j in range(len(list3[i])):
            print(f' {list3[i][j]:<{maxes[j+1]}} |', end='')
        print()
    
format_table(["best case", "worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.5345345345346, 2.00], [3.3, 2.9, 3.9]]) 