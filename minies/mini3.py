matrix = []
for numbers in input().split("|"):
    matrix.append(numbers.split())
for j in range(len(matrix)):
    for i in range(len(matrix[j])):
        print(int(matrix[j][i]), end=' ')
    print()  # please help
