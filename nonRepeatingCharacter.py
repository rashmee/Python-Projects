# coding=utf-8
#Find the first non repeating character

def first_non_repeating_char(str):
	for character in str:
		if str.count(character) > 1:
			continue
		else:
			return character
	return -1

print first_non_repeating_char("oohay")
print first_non_repeating_char("abccba")
