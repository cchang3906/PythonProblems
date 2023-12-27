class user:
	def __init__(self, first_name, last_name, location, age):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		print(f"Name: {self.first_name.title()} {self.last_name.title()}, Location: {self.location}, Age: {self.age}")

	def greet_user(self):
		print(f"Hello, {self.first_name.title()}!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

new_user = user('chris', 'chang', 'texas', 16)
new_user.describe_user()
new_user.greet_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)
