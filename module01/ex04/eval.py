class Evaluator:
	def __init__(self) -> None:
		pass

	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1

		coefs = tuple(coefs)
		words = tuple(words)
		zip_eva = list(zip(coefs, words))
		total_sum = 0
		for i in zip_eva:
			sum = i[0] * len(i[1])
			total_sum += sum
		print(total_sum)

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		
		coefs = tuple(coefs)
		words = tuple(words)
		enu_eva = list(enumerate(words))
		data_as_list = [list(item) for item in enu_eva]

		print(data_as_list)

		for index, item in enumerate(data_as_list):
			item[0] = coefs[index]

		print(data_as_list)
		total_sum = 0
		for i in data_as_list:
			sum = i[0] * len(i[1])
			total_sum += sum
		print(total_sum)





words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)

