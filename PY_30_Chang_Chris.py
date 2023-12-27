class user:
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def describe_user(self):
		print(f"Name: {self.first_name.title()} {self.last_name.title()}, Location: {self.location}, Age: {self.age}")

	def greet_user(self):
		print(f"Hello, {self.first_name.title()}!")

class privileges:
	def __init__(self):
		self.privileges = ["can add post", 'can delete post', 'can ban user']

	def show_privileges(self):
		print(f"These are the privileges of an admin:")
		for priv in self.privileges:
			print(f"-\t{priv.title()}")

class admin(user):
	def __init__(self, first_name, last_name, age):
		super().__init__(first_name, last_name, age)
		self.privileges = privileges()




mod = admin('chris', 'chang', 16)
mod.privileges.show_privileges()


