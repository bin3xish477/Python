from dataclasses import dataclass

"""
Seperating the collection data from the iterator that
iterates of that data. This is done for efficiency by
removing the need to reinitialize data every time we 
want to iterate over it.
"""

@dataclass
class Cities:
    _cities:tuple = ('Paris', 'Berlin', 'Rome', 'Madrid', 'London')
    _index:int = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return CityIterator(self)

class CityIterator:
    def __init__(self, city_obj):
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item

if __name__ == '__main__':
    cities = Cities()
    for c in cities:
        print(c)

