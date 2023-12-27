dinner = ['kobe bryant', 'shaq o neal', 'joey jordison']

print(f"{dinner[0].title()}, I invite you to dinner.")
print(f"{dinner[1].title()}, I invite you to dinner.")
print(f"{dinner[2].title()}, I invite you to dinner.")

print(f"\nUnfortunately, {dinner[2].title()} cannot come.")

dinner[2] = 'steph curry'


print(f"{dinner[0].title()}, {dinner[1].title()}, {dinner[2].title()}, I invite you all to dinner.")

print(f"\nI have found a bigger dinner table!")
dinner.insert(0, 'jarad higgins')
dinner.insert(2, 'john kang')
dinner.append('tony hu')

print(f"{dinner[0].title()}, {dinner[1].title()}, {dinner[2].title()}, {dinner[3].title()}, {dinner[4].title()}, {dinner[5].title()}, I invite you all to dinner.")

print(f"\nUnfortunately, the dinner table will be arriving late and we will only have two seats available.")

print(f"I am sorry {dinner.pop().title()} wont be able to join us.")
print(f"I am sorry {dinner.pop().title()} wont be able to join us.")
print(f"I am sorry {dinner.pop().title()} wont be able to join us.")
print(f"I am sorry {dinner.pop().title()} wont be able to join us.")

print(f"\n{dinner[0].title()}, and {dinner[1].title()} will still be invited.")

del dinner[1]
del dinner[0]

print(f"\nRemaining list: {dinner}")