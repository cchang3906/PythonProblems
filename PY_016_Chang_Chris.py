num = []
num1 = input("Enter the first number: ")
num.append(int(num1))
num2 = input("Enter the second number: ")
num.append(int(num2))
num3 = input("Enter the third number: ")
num.append(int(num3))
num4 = input("Enter the fourth number: ")
num.append(int(num4))
num5 = input("Enter the fifth number: ")
num.append(int(num5))
for number in num:
	for i in range(2, 6):
		if number%i==0:
			print(f'{number} is divisible by {i}.')

