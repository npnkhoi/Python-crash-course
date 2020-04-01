import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'D:\CodeHub\Python Crash Course\Weather Analyse\sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	print(reader)

	header = next(reader)
	for index, header in enumerate(header):
		print(index, header)

	highs, lows, dates = [], [], []
	for row in reader:
		try:
			time = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except:
			print("missing data")
		else:
			dates.append(time)
			highs.append(high)
			lows.append(low)
# print(dates)

# plot data
figure = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='r', linewidth = 0.4)
plt.plot(dates, lows, c='b', linewidth = 0.4)
plt.fill_between(dates, highs, lows, color='grey', alpha=0.1)
plt.tick_params(axis='both', which='major', labelsize = 10)

# format plot
plt.title("Daily temparature ranges in Sitka - 2014", fontsize = 24)
plt.ylabel('Temparature')
figure.autofmt_xdate()
plt.show()