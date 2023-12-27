sandwich_orders = ['ham', 'cheese', 'vegan', 'chicken', 'sausage']
finished_sandwiches = []
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f'I made your {current_sandwich} sandwich.')
	finished_sandwiches.append(current_sandwich)

print('I have finished these sandwiches:')
for i in range(0, 5):
	print(f'{finished_sandwiches[i].title()} sandwiches')