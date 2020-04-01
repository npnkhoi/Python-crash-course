from random import choice, randrange, randint
import matplotlib.pyplot as plt
import time

class RandomWalk():
	def __init__(self, num_points=5000):
		self.num_points = num_points

		self.x_values = [0]
		self.y_values = [0]

	def walk(self):
		while len(self.x_values) < self.num_points:
			x_dir = choice([-1, 1])
			x_len = choice([0, 1, 2, 3, 4])

			y_dir = choice([-1, 1])
			y_len = choice([0, 1, 2, 3, 4])

			if (x_len == 0) and (y_len == 0):
				continue

			self.x_values.append(self.x_values[-1]+x_dir*x_len)
			self.y_values.append(self.y_values[-1]+y_dir*y_len)

	def show(self):
		plt.scatter(self.x_values, self.y_values, s = 1)
		plt.show

	def save(self, name):
		# plt.scatter(self.x_values, self.y_values, s = 1, color = color = choice(['b', 'g', 'r', 'c', 'm', 'y', 'k']))
		point_numbers = list(range(self.num_points))
		plt.figure(dpi=128, figsize=(10, 6))

		plt.scatter(self.x_values, self.y_values, s = 1, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none')
		plt.scatter(0, 0, s = 10, color = 'k')
		plt.scatter(self.x_values[-1], self.y_values[-1], s = 10, color = 'r')

		# plt.axes().get_xaxis().set_visible(False)
		# plt.axes().get_yaxis().set_visible(False)
		# plt.show()
		plt.savefig('D:\CodeHub\Python Crash Course\Random Walk\\' + name + '.svg')
		plt.close()

for i in range(0, 100):
	print('start', i)
	rw = RandomWalk(50000)
	rw.walk()
	rw.save(str(i))
	print("finish", i)
