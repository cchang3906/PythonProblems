msgs = ['Never forget how worthless they made you feel.', \
"Successful people aren't defined by their success, but from how they respond to failure.", \
 "Don't wait for the opportunnity, create it.", \
 "Don't count the days, make the days count."]

names = ['Kyle', 'Brady', 'Steve', 'Chris']

def build_messages(name, msg):
	diction = {}
	for i in range(0, len(msg)):
			diction[name[i]] = msg[i]
	return diction

def print_messages(diction):
	for name, msg in diction.items():
		print(f'Hey {name.title()}: {msg}')

print_messages(build_messages(names, msgs))