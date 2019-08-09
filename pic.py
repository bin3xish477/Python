import pickle

a = [1,2,3,4,5,6,7,8,9]
with open('pickle.txt', 'wb') as pic:
	pickle.dump(a, pic)

with open('pickle.txt', 'rb') as pic:
	file = pickle.load(pic)
	print(file)