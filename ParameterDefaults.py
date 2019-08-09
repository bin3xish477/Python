def add_item(name, quantity, unit=1, grocery_list=None):
	if not grocery_list:
		grocery_list = []

	grocery_list.append(f"{name} ({quantity} {unit})")
	return grocery_list

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)
print(store1)
store2 = add_item('python', 1, 'medium-rare')
print(store2)

def factorial(n, cache = {}):
	if n < 1:
		return 1
	elif n in cache:
		return cache[n]
	else:
		print(f"calculating {n}!")
		result = n * factorial(n-1, cache = cache)
		cache[n] = result
		return result


print(factorial(3))
print(factorial(4))
print(factorial(5))