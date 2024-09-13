import sys

def whatis(int):
	if int == 0:
		print("I'm Zero.")
	elif int % 2 == 0:
		print("I'm Odd.")
	else:
		print("I'm Even.")


def main():
	assert len(sys.argv) > 1, "provide a argument"
	assert len(sys.argv) < 3, "more than one argument are provided"
	number = sys.argv[1]
	if number.isdigit():
		number = int(number)
	else:
		raise ValueError("argument is not an integer")
	whatis(number)

if __name__ == "__main__":
	main()
