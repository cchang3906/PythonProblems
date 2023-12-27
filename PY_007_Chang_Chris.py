cubes = [value**3 for value in range(1, 11)]
print(cubes)

odd = [value for value in range(1, 1000000, 2)]
print(f"MIN: {min(odd)}\tMAX:{max(odd)}")