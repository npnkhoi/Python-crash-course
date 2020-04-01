from pygal.maps.world import World, COUNTRIES

wm = World()
wm.title = 'Worldmap!'

# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('D:\CodeHub\Python Crash Course\Population\worldmap.svg')