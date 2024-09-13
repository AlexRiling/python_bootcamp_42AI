import sys

def text_transform(str) -> str:
	pass

def main():
	assert len(sys.argv) > 1, "Pass at least one str"

	text = ""

	for i in range(1, len(sys.argv)):
		text = text + " " + sys.argv[i]

	text = text[::-1]

	print(text.swapcase())

	text_transform(text)

if __name__ == "__main__":
	main()
