'''
Alexis Rodriguez
Python: Nested list
15 July 2019
'''

'''
list = []
dictionary = {}
tuples = ()
'''
nested_list = [[1,2,3], [4,5,6], [7,8,9]]

for i in nested_list:
  for j in i:
    print(j)
# list comprehension nested list
# the following line does the same as the above loops
[[print(j) for j in i] for i in nested_list]
# another example
board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)
board = [["x" if num % 2 != 0 else "o" for num in range(1,4)] for val in range(1,4)]
print(board)
nested_list = [[num for num in range(3)] for num in range(3)]
print(nested_list)
