import time

def ft_tqdm(lst: range) -> None: # type: ignore
    total = len(lst)
    total_bar_length = 30

    for elem in lst:
        percentage = (elem + 1) / total * 100
        filled_length = int(percentage / 100 * total_bar_length)
        filled_bar = filled_length * '='
        empty_bar = (total_bar_length - filled_length) * '-'

        print(f"\r({percentage:.2f} %) | [{filled_bar}{empty_bar}] | {elem + 1}/{total}", end="")

        yield elem


def main():
	for elem in ft_tqdm(range(79)):
		time.sleep(0.101)
	print()

if __name__ == "__main__":
	main()
