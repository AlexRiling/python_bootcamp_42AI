def ft_map(function_to_apply, iterable):
    if not callable(function_to_apply):
        raise TypeError(f"{function_to_apply} is not a callable function")

    try:
        iter(iterable)  # Ensure it's an iterable
    except TypeError:
        raise TypeError(f"{iterable} is not an iterable")

    # Return a generator, which applies the function lazily
    return (function_to_apply(item) for item in iterable)


def main():
	x = [1, 2, 3, 4, 5]
	print(ft_map(lambda dum: dum + 1, x))

	print(list(ft_map(lambda t: t + 1, x)))



if __name__ == "__main__":
	main()
