
def all_thing_is_obj(object: any) -> int:
	object_type = object.__class__
	if (object_type is int):
		print("Type not found")
	elif (object_type is str):
		print(object, "is in the kitchen", ":", object_type)
	else:
		print(object_type.__name__, ":", object_type)
	return 42