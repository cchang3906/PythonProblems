pizzas = ['cheese', 'beef', 'pepperoni']
for pizza in pizzas:
	print(f'I like {pizza} pizza.')

friend_pizzas = pizzas[:]

pizzas.insert(3, 'chicken')
friend_pizzas.insert(3, 'pineapple')
print('\nMy favorite pizzas are:')
for pizza in pizzas:
	print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())
