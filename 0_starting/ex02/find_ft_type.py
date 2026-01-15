def all_thing_is_obj(object: any) -> int:
	if object is None:
		return 42	
	type_name = type(object).__name__

	if type_name in ('list', 'tuple', 'set', 'dict'):
		print(f"{type_name.capitalize()} : {type(object)}")
	elif type_name == 'str':
		print(f"{object} is in the kitchen : {type(object)}")
	else:
		print("Type not found")
	return 42
