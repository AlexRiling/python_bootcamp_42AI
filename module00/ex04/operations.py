import sys

def operations(A: int, B: int):
	print(f"Sum:		{A + B}")
	print(f"Difference:	{A - B}")
	print(f"Product:	{A * B}")
	if B != 0:
		print(f"Quatient:	{A / B}")
		print(f"Remainder:	{A % B}")
	else:
		print("Quotient:	ERROR (division by zero)")
		print("Remainder:	ERROR (modulo by zero)")


def main():
	# error hadling
	assert len(sys.argv) == 3, """
	Usage: python operations.py <number1> <number2>
	Example:
		python operations.py 10 3
	"""

	A = sys.argv[1]
	B = sys.argv[2]

	try:
		A = int(A)
		B = int(B)
	except ValueError:
		raise ValueError("Error: only integers are allowed.")

	operations(A, B)

if __name__ == "__main__":
	main()
