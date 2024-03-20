import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dsensor
import datetime as dt

#creatin a figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

#init distance sensor
dsensor.dist()
distance = dist.distance_cm1
print(distance_cm1)
def animate(i, xs, ys):
	distance = round(dist.distance_cm1(), 2)

	xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
	ys.append(distance)

	ax.clear()
	ax.plot(xs, ys)

#format plot
	plt.xticks(rotation=45, ha='right')
	plt.subplot_adjust(bottom=0.30)
	plt.title('distance')
	plt.label('Distance CM')


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
