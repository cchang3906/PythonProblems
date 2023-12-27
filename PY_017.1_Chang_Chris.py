#conditional
msg = ""
while msg!="quit":
	msg = input('Enter pizza toppings that you want.\nEnter "quit" to terminate the program.')
	if msg!="quit":
		print(f"I'll add {msg} to your pizza.")