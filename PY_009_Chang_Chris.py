names_1 = ['harry', 'voldemort', 'hermione', 'belltrix', 'draco', 'remus', 'serverus']
names_2 = ['sirius', 'ron', 'hermione', 'draco', 'severus', 'dobby', 'remus']
the_name = 'hermione'

if the_name in names_1 and the_name in names_2:
	print(f"{the_name.title()} is in both lists.\n")

for name in names_1:
	if name not in names_2: 
		print(f"{name.title()} is only in the 1st list.")
print('\n')
for name in names_2:
	if name not in names_1: 
		print(f"{name.title()} is only in the 2nd list.")