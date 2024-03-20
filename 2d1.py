import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gpiozero import DistanceSensor
from time import sleep
import datetime as dt

# Creating a figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initializing distance sensor
def dist():
    sensor1 = DistanceSensor(echo=18, trigger=17)
    while True:
        distance_cm1 = sensor1.distance * 100
        yield distance_cm1  # Using yield to return distance_cm1 values continuously

def animate(i, xs, ys):
    distance = next(dist())  # Get the next distance_cm1 value

    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(distance)

    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Distance')
    plt.ylabel('Distance CM')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
