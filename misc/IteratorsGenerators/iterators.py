from dataclasses import dataclass

# creating an iterator object
@dataclass
class Squares(object):
    length:int
    i:int = 0

    # implementing the iterator protocol: __next__, __iter__
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i +=1
            return result

    def __iter__(self):
        return self

sq = Squares(10)
for item in sq:
    print(item)

# after the loop above the iterator object is exhausted
# and connot can be iterated over anymore
# the following line should print an empty string
# because the iterator has been exhausted
print("Exhausted iterator returns: ", end="")
print([item for item in sq])

# reinitializing the consumed iterator and using methods
# that expect an iterator such the `enumerate` function
sq = Squares(5)
for index, item in enumerate(sq):
    print(index, item)

# or `sorted`
sq = Squares(7)
print(sorted(sq, reverse=True))