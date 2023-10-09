x = 13.3
print(type(x))  # <class 'float'>

x = 10 + 2j
y = -3.0 - 33j
print(x+y) # (7-31j)
print(x**y) # (-0.16081129986272102-0.615349505780412j)

xs = [1, 2, 3]
print(type(xs)) # <class 'list'>
print(xs[0]) # 1
print(len(xs)) # 3
xs[1] = 33
print(xs) # [1, 33, 3]

ys = [5, True, 3.0, 2 + 2j]
print(type(ys)) # <class 'list'>
print(xs + ys) # [1, 33, 3, 5, True, 3.0, (2+2j)]

xs = [1, 2]
x = xs.pop # 2
print(xs) # [1]
