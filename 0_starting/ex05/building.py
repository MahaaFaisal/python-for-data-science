import sys

def count_by_condition(string: str, condition) -> int:
	"""Returns the count of characters based on a specific condition.
	
	string --  the text to evaluate
	condition -- a function that takes a character and returns True if the character meets the condition
	"""

	count = 0
	for c in string:
		if condition(c):
			count = count + 1
	return count

def get_input_string() -> str:
	if len(sys.argv) == 1:
		print("What is the text to count?")
		return (sys.stdin.read())
	elif (len(sys.argv) == 2):
		return (sys.argv[1])
	else:
		raise ValueError("Only one argument is allowed") 

def main():
	try:
		string = get_input_string()

		print("The text contains {} characters:".format(len(string)))
		print(count_by_condition(string, lambda c: c.isupper()), "upper letters")
		print(count_by_condition(string, lambda c: c.islower()), "lower letters")
		print(count_by_condition(string, lambda c: c in ".,;:?!"), "punctuation marks")
		print(count_by_condition(string, lambda c: c.isspace()), "spaces")
		print(count_by_condition(string, lambda c: c.isdigit()), "digits")

	except Exception as e:
		print(e.__class__.__name__, ":", e)

if __name__ == "__main__":
	main()