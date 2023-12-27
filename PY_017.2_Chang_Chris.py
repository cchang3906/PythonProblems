#break
msg = ""
while True:
	msg = input('Enter a list of pizza toppings that you want.\nEnter "quit" to terminate the program.')
	if msg!="quit":
		print(f"I'll add {msg} to your pizza.")
	if msg=='quit':
		break