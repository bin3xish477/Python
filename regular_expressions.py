#!/usr/bin/env python3

import re

test_string = r"123abc456789abc123ABC"

# Compiling string to use for searching.
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
	print(match)

# Same output as above.
matches = re.finditer(r"abc", test_string)

for match in matches:
	print(match)

# Match looks for patterns at the beginning of the string.
match = pattern.match(test_string)
print(match)

# Search will find the first occurrence of the pattern
match = pattern.search(test_string)
print(match)

# Find all will return a list of all the occuring strings that match
# the pattern specified.
match = pattern.findall(test_string)
print(match)

# Match object methods
match = pattern.finditer(test_string)
for m in match:
	# Print all the first and last index of found string
	print(m.span(), m.start(), m.end())
	# Print the actual value of the string
	print(m.group())

# . means any character excluding newlines.
# Use \. to find period in actual string.
pattern = re.compile(r".")
match = pattern.findall(test_string)
print(match)

# ^ is used to check if string is at the beginning of the string
pattern = re.compile(r"^123")
match = pattern.findall(test_string)
print(match)

# $ is used to check if string is at the end of the string
pattern = re.compile(r"ABC$")
match = pattern.findall(test_string)
print(match)

# Search for digits 0-9 that that appear 1 to 3 times
pattern = re.compile(r"\d{1,3}")
match = pattern.findall(test_string)
print(match)




