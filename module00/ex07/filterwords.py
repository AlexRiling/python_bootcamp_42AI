import sys

def filterwords(S: str,N: int):
	filtered_S = ''.join([char if char.isalpha() or char == " " else '' for char in S])

	words = [word for word in filtered_S.split() if len(word) > N]

	print(words)


def main():
	try:
		assert len(sys.argv) == 3, "ERROR"

		filterwords(sys.argv[1], int(sys.argv[2]))

	except AssertionError:
		print("ERROR")



if __name__ == "__main__":
	main()
