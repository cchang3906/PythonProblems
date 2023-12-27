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


name_loc = [
["La Traila #2", "8143 Mesa Dr, Austin, TX 78759" ],
["La Traila #3", "8224 Burnet Rd, Austin, TX 78757"],
["La Traila #4", "4912 Monterey Oaks Blvd, Austin, TX 78749"]
]
stores = []
for data in name_loc:
     stores.append(resturant(data[0], "Mexican Cuisine", data[1]))

for res in stores:
	res.describe_resturant()
	res.open_resturant()
