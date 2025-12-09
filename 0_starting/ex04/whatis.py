import sys

def odd_or_even(number: int) -> None:
	if (number % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")

try:
	argv = sys.argv
	assert len(argv) == 2, "AssertionError: more than one argument is provided"
	assert argv[1].isdigit() or (argv[1].startswith('-') and argv[1:].isdigit()), "AssertionError: argument is not an integer" 
	odd_or_even(int(argv[1]))

except Exception as e:
	print (e)

