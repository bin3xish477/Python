from math import factorial
from dataclasses import dataclass

@dataclass
class Factiter:
    len:int
    i:int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.len:
            raise StopIteration
        else:
            result = factorial(self.i)
            self.i += 1
            return result

# this function does exactly the same thing as the class
# defined above
def fact(n):
    for i in range(n):
        yield factorial(i)

if __name__ == "__main__":
    factorial_iter = Factiter(7)
    print(list(factorial_iter))

    generator = fact(7)
    print(list(generator))

    # `__iter__` and  `__next__` are both in dir(generator)
    # because of the `yield` keyword in the function fact


