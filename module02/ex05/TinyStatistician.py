
class TinyStatistician():
	def __init__(self):
		try:
			import numpy as np
			self.is_np_available = True
			self.np = np
		except ImportError:
			self.is_np_available = False

	def is_valid_input(self, x):
		if not isinstance(x, list) and (not self.is_np_available or not isinstance(x, self.np.ndarray)) or len(x) == 0:
			return False
		return True

	def bubble_sort(self, x):
		for i in range(0, len(x)):
			swapped = False
			for j in range(1, len(x)):
				if x[j] < x[j - 1]:
					x[j], x[j - 1] = x[j - 1], x[j]
					swapped = True
			if not swapped:
				break
		return x


	def mean(self, x):
		if not self.is_valid_input(x):
			return None

		result = 0
		for i in x:
			result += i
		return (result / len(x))

	def median(self, x):
		if not self.is_valid_input(x):
			return None

		x = self.bubble_sort(x)

		mid = len(x) // 2

		if not len(x) % 2 == 0:
			return x[mid]
		else:
			return (x[mid] + x[mid - 1]) / 2

	def quartile(self, x):
		if not self.is_valid_input(x):
			return None

		x = self.bubble_sort(x)
		n = len(x)

		q1_pos = (n - 1) / 4
		q1 = (x[int(q1_pos)] + x[int(q1_pos) + 1]) / 2 if q1_pos % 1 != 0 else x[int(q1_pos)]

		q3_pos = 3 * (n - 1) / 4
		q3 = (x[int(q3_pos)] + x[int(q3_pos) + 1]) / 2 if q3_pos % 1 != 0 else x[int(q3_pos)]

		return [float(q1), float(q3)]

	def var(self, x):
		if not self.is_valid_input(x):
			return None

		mean = self.mean(x)
		squared_diffs = [(i - mean) ** 2 for i in x]
		return self.mean(squared_diffs)

	def std(self, x):
		if not self.is_valid_input(x):
			return None

		return self.var(x) ** 0.5



def main():
	tstat = TinyStatistician()
	a = [1, 42, 300, 10, 59]
	print(tstat.mean(a))
	# Expected result: 82.4
	print(tstat.median(a))
	# Expected result: 42.0
	print(tstat.quartile(a))
	# Expected result: [10.0, 59.0]
	print(tstat.var(a))
	# # Expected result: 12279.439999999999
	print(tstat.std(a))
	# # Expected result: 110.81263465868862

if __name__ == "__main__":
	main()

