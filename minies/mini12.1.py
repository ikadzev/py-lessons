def cycle(lst):
    while True:
        yield from lst

for i in cycle([1, 2, 3]):
    print(i)
