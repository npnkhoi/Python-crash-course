import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

res = (r.json())["items"]

print(len(res))
num_rep = 100
cnt_rep = 0

# print(type(res))
names, repos = [], []
for rep in res:
	repo = {
		"value": rep["stargazers_count"],
		"label": str(rep["description"]),
		"xlink": rep["html_url"],
	}
	names.append(rep['name'])
	repos.append(repo)
	# print(rep["name"], repo, '\n')
	
	cnt_rep += 1
	if cnt_rep == num_rep:
		break

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.show_legend = False
my_config.title_font_size = 24
my_config.show_y_guides = False
my_config.x_label_rotation = 45

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most starred repos on github'
chart.x_labels = names
chart.y_title = 'stargazers_count'
chart.add('', repos)

chart.render_to_file('D:\CodeHub\Python Crash Course\API\python_repos.svg')
