#active variable
active = True
while active==True:
	msg = input("Enter your age.\nEnter '0' to terminate the program.")
	msg = int(msg)
	if msg!=0:
		if msg < 3:
			print("The ticket is free.")
		elif msg < 12:
			print("The ticket is $10.")
		else:
			print("The ticket is $15")
	else:
		active = False
