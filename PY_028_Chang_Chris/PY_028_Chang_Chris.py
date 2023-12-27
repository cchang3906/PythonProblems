from PY_028_Die_Chang_Chris import Die


six_SidedDie = Die()
ten_SidedDie = Die(10)
twenty_SidedDie = Die(20)
for i in range(10):
	six_SidedDie.roll_die()
print()
for i in range(10):
	ten_SidedDie.roll_die()
print()
for i in range(10):
	twenty_SidedDie.roll_die()