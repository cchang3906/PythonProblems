cities = {'austin':{'country':'USA', 'population':'965000', 'fun fact':'I live here.'}, 'dallas':{'country':'USA', 'population':'1.3M', 'fun fact':'3 hours away from Austin'}, 'houston':{'country':'USA', 'population':'2.3M', 'fun fact':'Tony lives here.'}}
for name, facts in cities.items():
	print(f'{name.title()}:')
	print(f"Country: {facts['country']}")
	print(f"Population: {facts['population']}")
	print(f"Fun fact: {facts['fun fact']} \n")