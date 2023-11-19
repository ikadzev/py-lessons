class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step
    def increment(self):
        self.count += self.step
        
# past_cls = None
# 
# def singleton(cls):
#     global past_cls
#     if not past_cls:
#         past_cls = cls
#     print(past_cls)
#     return past_cls
# 
# @singleton
# class GlobalCounter(Counter):
#     pass

# ВЫШЕ попытка сделать через декоратор


class Singleton:
    singleton = None
    # def __init__(self, *args, **kwargs):
    #     # print('self' if self else 'error with self!', 'and singleton eq to self' if Singleton.singleton == self else 'and singelton not eq to self' if Singleton.singleton else 'and singleton is none')
    #     if not Singleton.singleton:
    #         # print('Standart init')
    #         super().__init__(*args, **kwargs)
    #         Singleton.singleton = self
    #     else:
    #         # print('Singelton init')
    #         self = Singleton.singleton
    #     # print('self' if self else 'error with self!', 'and singleton eq to self' if Singleton.singleton == self else 'and singelton not eq to self' if Singleton.singleton else 'and singleton is none')
    def __new__(cls):
        if not cls.singleton:
            cls.singleton = super().__new__(cls)
        return cls.singleton

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

print(vars(gc1))
gc1.increment()
print(vars(gc2))
gc2.increment()
print(vars(gc1))

assert id(gc1) == id(gc2)