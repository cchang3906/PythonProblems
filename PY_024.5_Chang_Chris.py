def seat_guest(name, tables):
   lst = 4
   l_table = ''
   for table, members in tables.items():
      if len(members) < lst:
         lst = len(members)
         l_table = table
   if l_table != '':
      tables[l_table].append(name)

def print_table_seating(tables):
   for table, members in tables.items():
      print(f'Guests at {table} are:')
      for member in members:
         print(f'-\t{member.title()}')



tables = {
   'table 1': ['arvin', 'praveen', 'yasmine', 'amani'],
   'table 2': ['janie', 'yechang', 'dreymond'],
   'table 3': ['celine','jacob', 'aisha'],
   'table 4': ['tyrrell','ying'],
 }

while True:
   total = 0
   name = input("What is your name?:")
   seat_guest(name, tables)
   print_table_seating(tables)
   for table in tables.values():
      total += int(len(table))
   if total == 16:
      print("All tables are full.")
      break