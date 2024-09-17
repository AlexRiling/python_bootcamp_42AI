def ft_reduce(function_to_apply, iterable):
	if len(iterable) < 2:
		return iterable[0]
	elif len(iterable) == 0:
		raise TypeError("ft_reduce() of empty sequence with no initial value")

	result = function_to_apply(iterable[0], iterable[1])

	for i in range(2, len(iterable)):
		result = function_to_apply(result, iterable[i])

	return result


def main():
	lst = [1, 2, 3, 4, 5]
	print(ft_reduce(lambda u, v: u + v, lst))
	print(list(ft_reduce(lambda u, v: u + v, lst)))


if __name__ == "__main__":
	main()
