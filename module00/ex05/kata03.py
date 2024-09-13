kata = "The right format"

def kata03(string):
	backslash = "-" * (42 - len(string))
	print(backslash + string)

def main():
	kata03(kata)

if __name__ == "__main__":
	main()
