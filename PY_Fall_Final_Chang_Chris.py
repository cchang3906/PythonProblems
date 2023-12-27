#1
def revise_list(list, cmd, item, place=None):
	if cmd =='remove':
		list.remove(item)
	if cmd == 'add':
		list.insert(place, item)

fruit = ['orange', 'grape', 'pineapple', 'cantaloupe']
print(fruit)
revise_list(fruit, 'add', 'strawberry', 3)
print(fruit)
revise_list(fruit, 'remove', 'grape')
print(fruit)

#2
inventory = {'purses':6, 'belts':14, 'bracelets':13, 'sunglasses':4}
while True:
	for key, value in inventory.items():
		print(f'There are {value} {key.title()}')

	ans = input("Enter 'add' to add a quantity of product,\nEnter 'quit' to end:")
	if ans.lower() == 'quit':
		break
	elif ans.lower() == 'add':
		prod = input('What product do you want to add?')
		quan = int(input('How many sunglasses do you want to add:'))
		for key in inventory:
			if key.lower() == prod.lower():
				inventory[key]+=quan

#3
class doctor:
	def __init__(self, name):
		self.name = name.title()

	def describe(self):
		print(f"Dr. {self.name} helps sick people get healthy.")

class specialist(doctor):
	def __init__(self, name, specialty):
		super().__init__(name)
		self.specialty = specialty

	def describe(self):
		print(f"Doctor {self.name} is a {self.specialty} that helps sick people get healthy.")

class hospital:
	def __init__(self, doctors):
		self.doctors = doctors

	def print_staff(self):
		for doc, spec in self.doctors.items():
			spec = specialist(doc, spec)
			spec.describe()

doc_and_type = {'Daniel Wilschetz':'heart surgeon', 'Scott Kim':'pediatrician', 'Kelly Fairman':'psychiatrist'}
clinic = hospital(doc_and_type)
clinic.print_staff()


