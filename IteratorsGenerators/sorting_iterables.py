from dataclasses import dataclass
from random import randint

@dataclass
class RandomInts(object):
    length:int
    lower:int = 0
    upper:int = 100

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.RandomIterator(self.length, self.lower, self.upper)

    @dataclass
    class RandomIterator(object):
        length:int
        lower:int
        upper:int
        requests:int = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.requests >= self.length:
                raise StopIteration
            else:
                r = randint(self.lower, self.upper)
                self.requests += 1
                return r
    

if __name__ == "__main__":
    randoms = RandomInts(10)
    for num in randoms:
        print(num)
