n = int(input("N? "))
print("Array?")
arr = [input() for _ in range(n)]
n1 = int(input("N1? "))
print("Seccond array?")
arr1 = [input() for _ in range(n1)]

print([(arr[i], arr1[i]) for i in range(0, min(n, n1))])
