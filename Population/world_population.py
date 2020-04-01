import json
from pygal.maps.world import World, COUNTRIES
from pygal.style import RotateStyle

def get_code(name):
	for x, y in COUNTRIES.items():
		if y == name:
			return x
	return None

filename = 'D:\CodeHub\Python Crash Course\Population\population_data.json'
with open(filename) as f:
	data = json.load(f)

wm = World(style = RotateStyle('#FF0000'))
wm.title = 'World population in 2010'

group1, group2, group3 = {}, {}, {}

for dict in data:
	if dict['Year'] == '2010':
		code = get_code(dict['Country Name'])
		if code == None:
			continue
		pop = int(dict['Value'])
		if pop < 10**7:
			group1[code] = pop
		elif pop < 10**9:
			group2[code] = pop 
		else:
			group3[code] = pop

# print(len(group1), len(group2), len(group3))

wm.add('>= 1B', group3)
wm.add('10M - <1B', group2)
wm.add('<10M', group1)

wm.render_to_file("D:\CodeHub\Python Crash Course\Population\world_population.svg")