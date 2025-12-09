import sys

def count_upper_case(string: str) -> int:
	count = 0
	for c in string:
		if (c.isupper()):
			count = count + 1
	return count


def count_lower_case(string: str) -> int:
	count = 0
	for c in string:
		if (c.islower()):
			count = count + 1
	return count

def count_punctuation(string: str) -> int:
	count = 0
	for c in string:
		if c in ".,;:?!":
			count = count + 1
	return count

def count_digits(string: str) -> int:
	count = 0
	for c in string:
		if (c.isdigit()):
			count = count + 1
	return count

def count_spaces(string: str) -> int:
	count = 0
	for c in string:
		if (c.isspace()):
			count = count + 1
	return count

def main():
	string = sys.argv[1]
	print("The text contains {} characters:".format(len(string)))

	print(count_upper_case(string), "upper letters")
	print(count_lower_case(string), "lower letters")
	print(count_punctuation(string), "punctuation marks")
	print(count_spaces(string), "spaces")
	print(count_digits(string), "digits")
	
if __name__ == "__main__":
	main()