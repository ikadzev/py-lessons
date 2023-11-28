def coroutine(f):
    def call_able(*args, **kwargs):
        f_temp = f()
        next(f_temp)
        return f_temp
    return call_able


@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(42))  # False
print(st.send(42))  # True
