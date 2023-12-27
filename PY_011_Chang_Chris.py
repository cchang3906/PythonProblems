current_users = ['aaron', 'charlie', 'kieran', 'finn', 'roman']
new_users = ['AARON', 'roman', 'zach', 'john', 'paul']
lower_new = []

for nuser in new_users:
	lower_new.append(nuser.lower())

for lnew in lower_new:
		if lnew in current_users:
			print("This username is used, please enter a new username.")
		else:
			print("This username is available.")