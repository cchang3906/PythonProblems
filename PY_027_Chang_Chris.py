class resturant:
	def __init__(self, resturant_name, cuisine_type, address):
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type
		self.address = address

	def describe_resturant(self):
		print(f"Resturant name: {self.resturant_name}")
		print(f"Cuisine type: {self.cuisine_type}")
		print(f"Address: {self.address}")

	def open_resturant(self):
		print(f"{self.resturant_name} is now open.")

class ice_CreamStand(resturant):
	def __init__(self, resturant_name, cuisine_type, address, flavors):
		super().__init__(resturant_name, cuisine_type, address)
		self.flavors = flavors

	def flavor_display(self):
		print(f"This store currently sells {self.flavors} flavors.")

Baskin_Robbins = ice_CreamStand('Baskin Robbins', 'Ice Cream', '730 W Stassney Ln Ste 155, Austin, TX', 'Chocolate, Strawberry, Vanilla, Mint')
Baskin_Robbins.flavor_display()