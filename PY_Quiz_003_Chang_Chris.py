#1
names = ['aisha', 'anish', 'ariaan', 'aisha', 'aditya', 'ariaan', 'avani', 'aisha', 'amar']
print(names)

while 'aisha' in names:
	names.remove('aisha')

print(names)

#2
def favorite_colors(name, *colors):
	print(f"{name.title()}'s favorite colors are:")
	for color in colors:
		print(f'\t{color}')

favorite_colors('brad', 'bronze', 'brown', 'black')
favorite_colors('tania', 'blue', 'green')

#3
num = 1
while num != 0:
	num = int(input("How old are you? Enter 0 to quit:"))
	if(num >= 50):
		ans = input("Do you want to play bingo? Yes or No:")
		if ans.lower() == 'no':
			print("Too bad.")
			continue
		elif ans.lower() == 'yes':
			print("Wonderful. Here's your scorecard.")