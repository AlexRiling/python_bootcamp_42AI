def ft_filter(function_to_apply, iterable):
	new_iterable = [item for item in iterable if function_to_apply(item)]
	return new_iterable

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

def main():
	ages = [5, 12, 17, 18, 24, 32]


	adults = filter(myFunc, ages)
	ft_adults = ft_filter(myFunc, ages)

	print("filter:\n")
	for x in adults:
		print(x)

	print("\n")

	print("ft_filter:\n")
	for x in ft_adults:
			print(x)



if __name__ == "__main__":
  main()
