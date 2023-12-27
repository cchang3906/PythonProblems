#1
names = ['Zendaya', 'anil', 'Frank', 'dylan', 'taylor']

names[1] = names[1].title()
names[3] = names[3].title()
names[4] = names[4].title()
names.sort(reverse=True)
print(names)

#2
names_1 = ['sierra', 'jen', 'don', 'athena']
names_2 = ['jada', 'lucas']

names_2.insert(0, names_1.pop())
names_2.remove('jada')

print(f'\nThe names in names_1 are:\n\t{names_1[0]}\t{names_1[1]}\t{names_1[2]}')
print(f'The names in names_2 are:\n\t{names_2[0]}\t{names_2[1]}')

#3
numbers = [1.5, 0, -3, 435.86, -0.765]
numbers.sort()
print(f'\n{numbers[0]}\t{numbers.pop()}')

#4
ikbalage = 2022 - 2008
seanage = 2022 - 2005

print(f'\nIkbal is {ikbalage} and Sean is {seanage}, and their combined age is {ikbalage + seanage}.')