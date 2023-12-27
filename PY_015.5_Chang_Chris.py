#1
my_advisory = ['maria', 'jorge', 'putnam', 'daniel', 'ibrahim', 'erin']
clubs = {'mock trial':['mike', 'kayla', 'ibrahim', 'rashida', 'nour', 'maria'], 'fishing club':['kamala', 'gloria', 'evelyn', 'kevin', 'jorge'], 'green goblins':['juan', 'maria', 'patricia', 'gloria', 'daniel', 'ibranhim']}
vals = []
for names in clubs.values():
	for name in names:
		vals.append(name)
for advisors in my_advisory:
		if vals.count(advisors) >=2:
			print(f'{advisors.title()} has a conflict.')
		elif vals.count(advisors)==0:
			print(f'{advisors.title()} is in no clubs.')

#2
numbers = [50, 3, -42, 81, 25, 14]
over_20 = [value for value in numbers if value>=20]
print(over_20)

#3
people = {'sam':1988, 'aneesa':1981, 'salman':1947, 'kim':1980, 'bell':1952, 'yuri':1934}
yr = sorted(people.values())
people_sort = {}
for num in yr:
	for name, year in people.items():
		if num==year:
			people_sort[name] = year
print(people_sort)

#4
names = ['Aaron', 'Devon', 'Shefaly', 'Terrance', 'North', 'Aizza']
for name in names[:3]:
	print(name.upper())
for name in names[-3:]:
	print(name.lower())

#5
list_of_lists = [[1, -9, 8], [], [-7, 9, 3, 4, -6, 0], [7, 10, 5, -2, 5]]
min_num = 0
max_num = 0
for number in list_of_lists:
	for num in number:
		if num > max_num:
			max_num = num
		elif num <min_num:
			min_num = num
print(max_num, min_num)
