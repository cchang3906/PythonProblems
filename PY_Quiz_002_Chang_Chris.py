#1
list_1 = ['jessica', 'heath', 'uma', 'robin', 'akira', 'jessica', 'cleo', 'uma']
list_2 = list_1[:3]
list_3 = list_1[5:8]
list_2.append('heath')
print(list_1)
print(list_2)
print(list_3)
for firstl in list_1:
	if firstl not in list_2 and firstl not in list_3:
		print(firstl)

print('\n')
#2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
	print(f'loop\t{num}')

print('\n')
#3
numbers = (5, -33.3, 3, -23, 0, 0.1, 18)
for num in numbers:
	if num >0:
		print(f'{num} is positive')
	elif num==0:
		print('0 is neither positive nor negative')
	else:
		print(f'{num} is negative')

print('\n')
#4
odds = [1, 3, 5, 7, 9]
evens = []
evens = [value+1 for value in odds]

print(evens)