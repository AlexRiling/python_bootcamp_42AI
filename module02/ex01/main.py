
def what_are_the_vars(*args, **kwargs):
	obj = ObjectC()

	# handling None
	if not args and not kwargs:
		return None

	# handling args
	list_of_args = [arg for arg in args]
	for i in range(0, len(list_of_args)):
		setattr(obj, f"var_{str(i)}", list_of_args[i])

	# handling kwargs
	kwarg_dir = {key: value for key, value in kwargs.items()}
	for key, value in kwarg_dir.items():
		if hasattr(obj, key):
			return None
		setattr(obj, key, value)

	return(obj)

class ObjectC(object):
	def __init__(self):
		pass


def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != "_":
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")


if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)
