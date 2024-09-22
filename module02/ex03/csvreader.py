class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if filename is not None and not isinstance(filename, str):
			raise ValueError(f"Expected 'filename' to be a string, got {type(filename).__name__}")

		if not isinstance(sep, str):
			raise ValueError(f"Expected 'sep' to be a string, got {type(sep).__name__}")

		if not isinstance(header, bool):
			raise ValueError(f"Expected 'header' to be a boolean, got {type(header).__name__}")

		if not isinstance(skip_top, int) or skip_top < 0:
			raise ValueError(f"Expected 'skip_top' to be a non-negative integer, got {type(skip_top).__name__}")

		if not isinstance(skip_bottom, int) or skip_bottom < 0:
			raise ValueError(f"Expected 'skip_bottom' to be a non-negative integer, got {type(skip_bottom).__name__}")

		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None

	def __enter__(self):
		try:
			self.file = open(self.filename, 'r')
		except FileNotFoundError:
			self.file = None

		if self.getdata() is None:
			self.file.close()
			self.file = None
			return None

		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if self.file:
			self.file.close()
		return False

	def getdata(self):
		data = []

		for line in self.file:
			row = line.strip().split(self.sep)
			row = [item.strip().strip('"') for item in row]

			if len(data) > 0 and len(row) != len(data[0]):
				return None

			data.append(row)

		if self.skip_top > 0:
			data = data[self.skip_top:]

		if self.skip_bottom > 0:
			data = data[:-self.skip_bottom]

		return data


	def getheader(self):
		if not self.header:
			return None

		self.file.seek(0)
		header_row = self.file.readline().strip().split(self.sep)
		header_row = [item.strip().strip('"') for item in header_row]

		return header_row


def main():
	with CsvReader('good.csv', header=True) as file:
		data = file.getdata()
		print(file.getheader())

	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")




if __name__ == "__main__":
	main()
