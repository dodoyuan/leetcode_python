
class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current

a = Squares(1, 100)
for b in a:
    print b

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

import functools
def singleton(f):
    instance = {}
    functools.wraps(f)
    def wrapper(*args, **kwargs):
        if f not in instance:
            instance[f] = f(*args, **kwargs)
        return instance[f]
    return wrapper()