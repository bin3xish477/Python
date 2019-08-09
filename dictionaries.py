'''
Alexis Rodriguez
Python: Dictionaries
15 July 2019
'''
# dictionary example:
instructor = {
"name": "Colt",
"owns_dog": True,
"num_courses": 4,
"favorite_language": "Pyton",
"is_hilarious": False,
44: "my favorite number!"
}
print()
print(instructor)
print()

# creating dictionary using dict method:
phoneNumbers = dict(alex=123456, ransel=8498772, martha=908774)
print(phoneNumbers)
print()
# extracting data from dictionary:
print(instructor['name'])
print(phoneNumbers['alex'])
print()
# retrieving all values from dictionary:
[print(value) for value in instructor.values()]
print()

#retrieving all keys from dictionary:
[print(key) for key in instructor.keys()]
print()

#accessing both values/keys in dictionary:
[print(item) for item in instructor.items()]
print()

'''
dictionary methods:
instructor.clear()
copy = phoneNumbers.copy()
{}.fromkeys("a", "b")
phoneNumbers.get('alex')
instructor.pop('owns_dog')
phoneNumbers.popitems()
instructor.update()
'''
