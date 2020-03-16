'''
Alexis Rodriguez
Python: Dictionary Comprehension
1 July 2019
'''
numbers = dict(first=1, second=2, third=3)
# creating new dictionary with same keys as numbers but squared values
squaredNumbers = {key: value**2 for key,value in numbers.items()}
print(squaredNumbers)
#other examples
dict = {num: pow(num,2) for num in range(1,6)}
print(dict)

str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range(len(str1))}
print(combo)
# dictionary definition
instructor = {
"name": "Colt",
"owns_dog": 'yes',
"favorite_language": "Pyton",
}
newInstructor = {k.upper(): v.upper() for k,v in instructor.items()}
print(newInstructor)
# conditional logic with dictionary comprehension
numList = [0,1,2,3,4,5,6,7,8,9]
numParity = {num: 'even' if num % 2 == 0 else 'odd' for num in numList}
print(numParity)
