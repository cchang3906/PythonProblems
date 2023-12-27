def enter_name():
	"""Takes player names"""
	names = []
	for i in range(0,2):
		name = input(f"What is player {i+1}'s name?")
		names.append(name)
	return names

def rules(name1, name2):
	"""Prints rules for TTT"""
	print(f'Welcome {name1.title()} and {name2.title()}! The rules for Tic Tae Toe are simple:\n\tPlayers will take turns marking the spaces in a three-by-three grid with X or O.\n\tThe player who places three marks in a horizontal, vertical, or diagonal row wins.\n\tThe grids are marked as A 1, A 2, A 3, B 1, B 2, B 3, etc.\n\tTo quit, enter "Quit" as the row. \nGood luck!')

def display_game(game):
	"""Displays the game grid"""
	for n in range(0,3):
		for i in range(0,3):
			print("\t|\t|")
			if i==1:
				print(f"    {game[n][0]}   |   {game[n][1]}   |    {game[n][2]}")
		if n == 2:
			break
		print("--------|-------|--------")
	

def victory(game):
	"""Determines if theres a winner"""
	for n in range(0,3):
		if game[n][1]!='.':
			if game[n][0]==game[n][1] and game[n][1]==game[n][2]:
				if game[n][0]=="X":
					return(1)
				else:
					return(2)
		if game[1][n]!='.':
			if game[0][n]==game[1][n] and game[1][n]==game[2][n]:
				if game[0][n]=="X":
					return(1)
				else:
					return(2)
		else:
			continue
	if game [1][1]!='.':
		if game[0][0]==game[1][1] and game[1][1]==game[2][2]:
			if game[1][1]=="X":
				return(1)
			else:
				return(2)
		elif game[0][2]==game[1][1] and game[1][1]==game[2][0]:
			if game[1][1]=="X":
				return(1)
			else:
				return(2)
	return(0)

def all_fill(game):
	"""Determines if all the grids are filled"""
	for n in range(0,3):
		for i in range(0,3):
			if game[i][n]=='.':
				return(False)
			else:
				continue
	return(True)

def turn(name1, name2, n):
	"""Displays player turn"""
	if n%2==0:
		print(f"It's {name1.title()}'s turn. {name1.title()} is O.")
	else:
		print(f"It's {name2.title()}'s turn. {name2.title()} is X.")

def player_input(row, column, n):
	"""Intakes player input"""
	if row.lower() != 'a' and row.lower() != 'b' and row.lower() != 'c':
		return(1)
	elif column > 3:
		return(2)
	if row.lower() =='a':
		for a in range(1,4):
			if column == a:
				if game[0][a-1]=='.':
					if n%2==1:
						game[0][a-1] = 'X'
					else:
						game[0][a-1] = 'O'
				else:
					return(1)
	elif row.lower() =='b':
		for a in range(1,4):
			if column == a:
				if game[1][a-1]=='.':
					if n%2==1:
						game[1][a-1] = 'X'
					else:
						game[1][a-1] = 'O'
				else:
					return(1)
	else:
		for a in range(1,4):
			if column == a:
				if game[2][a-1]=='.':
					if n%2==1:
						game[2][a-1] = 'X'
					else:
						game[2][a-1] = 'O'
				else:
					return(1)
	return(0)


names = enter_name()
rules(names[0], names[1])
game = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
n=1
while(victory(game)==0 and all_fill(game)==False):
	display_game(game)
	turn(names[0], names[1], n)
	row = ''
	column = None
	while(True):
		row = input("Enter row value: ")
		if row.lower() == "quit":
			break
		column = int(input("Enter column value: "))
		if player_input(row, column, n)==0:
			n+=1
			break
		elif player_input(row, column, n)==1:
			print(f"Invalid row value, please enter again.")
		elif player_input(row, column, n)==2:
			print(f"Invalid column value, please enter again.")
	if row.lower() == "quit":
		break
if victory(game)==2:
	print(f"{names[0].title()} is the winner! Good luck next time {names[1].title()}!")
elif victory(game)==1:
	print(f"{names[1].title()} is the winner! Good luck next time {names[0].title()}!")
elif row.lower() == "quit":
	print(f"A player has quit. Thank you for playing!")
else:
	print(f"The game is tied.")
print("Final board:")
display_game(game)


