from math import log2

n = int(input("Input number: "))
k = 0
if n != 0:
    for i in range(int(log2(abs(n))) + 2):
        k += 1 if (n & (1 << i) != 0) else 0
print(k)
