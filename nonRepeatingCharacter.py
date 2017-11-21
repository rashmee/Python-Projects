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
# print first_non_repeating_char("rashmee")
# print first_non_repeating_char("abac")
# print first_non_repeating_char("hygull")
# print first_non_repeating_char("abcabdcbdefg")
# print first_non_repeating_char("abccba")