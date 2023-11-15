def sum(x, y):
    return x + y


def specialize(f, *known_arg, **known_karg):
    return lambda *args, **kwargs: f(*args, *known_arg, **known_karg, **kwargs)


plus_one = specialize(sum, y=1)
print(plus_one(10))  # 11

just_two = specialize(sum, 1, 1)
print(just_two())  # 2
