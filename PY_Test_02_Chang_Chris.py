#1
purchases = [('shonna', 'car'), ('sanjay', 'car'), ('brenda', 'none'), ('tamu', 'house')]
for name, product in purchases:
	if product=='car':
		print(f'{name.title()}, I have a must-see auto insurance offer for you.')
	elif product=='house':
		print(f'{name.title()}, I have an incredile home insurance offer for you. ')
	elif product=='none':
		print(f'{name.title()}, I have a life insurance offer for you that will ease your worry.')

#2
numbers = [3, -14, -3, 2, 136, -49]
opp_numbers = [values*-1 for values in numbers]
print(f'{numbers}\n{opp_numbers}')

#3
people = [{'name':'akmed', 'age':34, 'hobby':'golf', 'state':'texas'}, \
{'name':'randy', 'pol_party':'independent', 'state':'texas', 'age':56}, \
{'name':'baozhai', 'age':62, 'state':'nevada', 'pol_party':'republican'}]
for ppl in people:
	if ppl['age']>=50 and ppl['state']=='texas':
		print(f"{ppl['name'].title()}, please join AARP.")

#4
list_of_lists = [[1, 3, -5, 4], [23, -49, -3], [], [-2, 5]]
for lst in list_of_lists:
	if len(lst)!=0:
		print(f'The first element in {lst[0]}, and the last element is {lst[-1]}.')
	else:
		print('The list is empty.')
