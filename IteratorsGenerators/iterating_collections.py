from dataclasses import dataclass
from random import randint
# s = {'x', 'y', 'b', 'c', 'a'}
# for item in s:
#     print(item)

# type error 'set object does not support indexing'
# print(s[0])


# infinite collection
# class Squares(object):
#     def __init__(self):
#         self.i = 0
#     # infinite collection
#     def next_(self):
#         result = self.i ** 2
#         self.i += 1
#         return result

# sq = Squares()
# for i in range(1, 11):
#     print(sq.next_())


# @dataclass
# class Squares(object):
#     length: int
#     i: int = 0

#     def __len__(self):
#         return self.length
#     # no longer an infinite collection
#     def next_(self):
#         if self.i >= self.length:
#             raise StopIteration
#         else:
#             result = self.i ** 2
#             self.i += 1
#             return result

# # sq = Squares(5)
# # print(f"Size of collection is {len(sq)}")
# # for i in range(1, 11):
# #     print(sq.next_())

# sq = Squares(10)
# while True:
#     try:
#         print(sq.next_())
#     except StopIteration:
#         print("Reached collection limit")
#         break


# implementing __next__ to use standard library `next()`
# @dataclass
# class Squares(object):
#     length: int
#     i: int = 0

#     def __len__(self):
#         return self.length
#     # no longer an infinite collection
#     def __next__(self):
#         if self.i >= self.length:
#             raise StopIteration
#         else:
#             result = self.i ** 2
#             self.i += 1
#             return result

# sq = Squares(5)
# while True:
#     try:
#         print(next(sq))
#     except StopIteration:
#         print("Reached collection limit...")
#         break


@dataclass
class RandomNumbers(object):
    length:int
    range_min:int = 0
    range_max:int = 10
    num_requested:int = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return randint(self.range_min, self.range_max)

numbers = RandomNumbers(10)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break
