import random

def generate_unique_random_numbers(n):
    numbers = list(range(n))

    # Fisher-Yates shuffle algorithm
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        # Swap numbers[i] with numbers[j]
        numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

def generator(text, sep=" ", option=None):
	try:
		list_of_text = text.split(sep)
	except AttributeError:
		print("ERROR")
		return 1

	if option is not "ordered" or "unique" or "shuffle":
		raise TypeError("ERROR")


	if option == "shuffle":
		list_of_random_numbers = generate_unique_random_numbers(len(list_of_text))
		for i in range(0, len(list_of_text)):
			yield list_of_text[list_of_random_numbers[i]]
	elif option == "unique":
		already_printed_list = []
		for i in list_of_text:
			if i not in already_printed_list:
				already_printed_list.append(i)
				yield i
		print(already_printed_list)
	elif option == "ordered":
		list_of_text = sorted(list_of_text)
		for i in list_of_text:
			yield i

text2 = "Lorem Ipsum Lorem Ipsum"
text = "Le Lorem Ipsum est simplement du faux texte."
text3 = 256
for word in generator(text, option="dered"):
	print(word)

