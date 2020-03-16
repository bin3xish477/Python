# function annotation
def my_func(a: str, b: 'int > 0') -> str:
	return a * b

#function docstrings
def func(a, b):
	"This function returns the addition of two integers"
	return a + b

#defautl values
def myFunction(a: str = 'xyz', b: int = 1) -> str:
	pass
