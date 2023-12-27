favorite_languages = {'jen':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}
poll_subjects = ['jen', 'sarah', 'john', 'tony', 'phil', 'jake']

for sub in poll_subjects:
	if sub in favorite_languages:
		print(f"Thank you {sub.title()}, for responding to the poll.")
	else:
		print(f"Hey {sub.title()}, you should take our poll.")