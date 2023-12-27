current_users = ['aaaaron8', 'charlie', 'kieran', 'finn', 'roman']
new_users = ['AAAARON8', '99celebration', '9Zachhh8', 'JohN12', 'Pauliton']


for nuser in new_users:
	if nuser.lower() in current_users:
		print("This user name is taken, please enter a new username.")
	elif len(nuser) < 8:
		print("Username needs to be longer than 7 characters.")
	elif nuser.isalpha()==True:
		print("A username requires at least one number.")
	elif nuser.islower()==True:
		print("A username requires at least one uppercase letter.")
	else:
		print("This username is available.")
