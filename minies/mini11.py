class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step
    def increment(self):
        self.count += self.step

class Singleton:
    singleton = None
    s_check = False
    s_vars = {}
    def __new__(cls, *args, **kwargs):
        if not Singleton.singleton:
            Singleton.singleton = super().__new__(cls)
        else:
            Singleton.s_check = True
            Singleton.s_vars = vars(Singleton.singleton).items()
        return Singleton.singleton
    def __init__(self, *args, **kwargs):
        if not Singleton.s_check:
            super().__init__(*args, **kwargs) # AAAAAAAAAAAAAA WHY ITS SO EASY

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter(1, 2)
print(vars(gc1))
gc1.increment()
print(vars(gc1))

gc2 = GlobalCounter()
print(vars(gc2))
gc2.increment()
print(vars(gc1))

assert id(gc1) == id(gc2)