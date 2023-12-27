birth_years = [('sam', 1998), ('aneesa', 1981), ('salman', 1947), ('kim', 1980), ('bell', 1952), ('yuri', 1934)]

for byr in birth_years:
	if byr[1] >= 1990:
		print(f"{byr[0]} was born in the 90s.")
	elif byr[1] >= 1980:
		print(f"{byr[0]} was born in the 80s.")
	elif byr[1] >= 1970:
		print(f"{byr[0]} was born in the 70s.")
	elif byr[1] >= 1960:
		print(f"{byr[0]} was born in the 60s.")
	elif byr[1] >= 1950:
		print(f"{byr[0]} was born in the 50s.")
	elif byr[1] >= 1940:
		print(f"{byr[0]} was born in the 40s.")
	else:
		print(f"{byr[0]} was born in the 30s.")
