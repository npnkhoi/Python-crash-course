from dice import Dice 
import pygal

def roll(times):
	ret = []
	while times > 0:
		times -= 1
		d = Dice()
		ret.append(d.roll())
	return ret

def cal_freq(list):
	freq = [0] * 6
	for i in list:
		freq[i - 1] += 1
	return freq

def visualize(list):
	hist = pygal.Bar()

	hist.title = 'Statistic on Dice Rolling'
	hist.y_title = 'Frequency'
	hist.x_title = 'Faces'
	hist.x_labels = ['1', '2', '3', '4', '5', '6']

	hist.add('D6', list)
	hist.render_to_file('D:\CodeHub\Python Crash Course\Dice Visual\die_visual.svg')

res = roll(10000)
freq = cal_freq(res)
print(freq)

visualize(freq)