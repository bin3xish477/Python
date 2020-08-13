'''
***************************
List Comprehension Practice
Alexis Rodriguez
5 July 2019
***************************
'''


numbers = [1,2,3,4,5,6,7,8,9,10]
num = [str(num) for num in numbers if num % 2 == 0]
print (num)

letter = [letter[0] for letter in ['Elie', 'Tim', 'Matt']]
letter2 = [value for value in [1,2,3,4,5,6] if value % 2 == 0]
print(letter)
print(letter2)

num = [num for num in [1,2,3,4] if num in [3,4,5,6]]
reverse = [word[::-1].lower() for word in ['Elie', 'Tim', 'Matt']]
print(num)
print(reverse)

dozen = [num for num in range(1,101) if num % 12 == 0]
print(dozen)

str = 'amazing'
nonVowels = [letter for letter in str if letter not in 'aeiou']
print(nonVowels)
