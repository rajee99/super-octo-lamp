from functools import wraps

def cached(func):
    cache = {}
    @wraps(func)
    def wrapper(x):
        return cache.setdefault(x, func(x))
    return wrapper

@cached
def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)

squares = (x*x for x in range(1, 11))

with open("out.txt", "w") as f: f.write(", ".join(map(str, squares)))

class AutoRepr(type):
    def __new__(m, n, b, d):
        d["__repr__"] = lambda self: f"{n}({vars(self)})"
        return super().__new__(m, n, b, d)

class Point(metaclass=AutoRepr):
    def __init__(self, x, y): self.x, self.y = x, y

print(Point(3, 4), fib(10))
