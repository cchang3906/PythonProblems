def build_sandwich(*ingred):
	"""accepts ingredients and prints desired sandwich"""
	print("You have requested a sandwich containing the following ingredients:")
	for ing in ingred:
		print(f'-\t{ing}')
	print('\n')

build_sandwich('ham', 'chicken')
build_sandwich('fried chicken', 'cheese', 'lettuce', 'tomato')
build_sandwich('cheese')

def make_car(manu, name, **optional):
	optional['manufact'] = manu
	optional['names'] = name
	return optional

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)