
def NULL_not_found(object: any) -> int:
	object_type = object.__class__
	if (object is None):
		print("Nothing: ", end="")
	elif (object.__class__ is float):
		print("Cheese: ", end="")
	elif (object.__class__ is int and object == 0):
		print("Zero: ", end="")
	elif (object.__class__ is str and not object):
		print("Empty: ", end="")
	elif (object.__class__ is bool and not object):
		print("Fake: ", end="")
	elif (object.__class__ is str and object):
		print("Type not Found")
		return 1
	
	print(object, object_type)
	
	if (object is None):
		return 0
	return 1
