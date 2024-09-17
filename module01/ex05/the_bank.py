
class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, "value"):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount



class Bank(object):
	def __init__(self):
		self.accounts = []


	def add(self, new_account):
		if not isinstance(new_account, Account):
			return False

		for account in self.accounts:
			if account.name == new_account.name:
				return False

		self.accounts.append(new_account)
		return True



	def transfer(self, origin_name, dest_name, amount):
		origin = None
		dest = None

		for account in self.accounts:
			if account.name == origin_name:
				origin = account
			if account.name == dest_name:
				dest = account

		if origin is None or dest is None:
			return False

		if not isinstance(amount, (int, float)) or amount < 0 or origin.value < amount:
			return False

		origin.value -= amount
		dest.value += amount

		return True


	def fix_account(self, name):
		pass


