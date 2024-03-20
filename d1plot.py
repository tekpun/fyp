from gpiozero import DistanceSensor
from time import sleep
import matplotlib.pyplot as plt

def dist():
    sensor1 = DistanceSensor(echo=18, trigger=17)
    distances = []  # List to store distance values
    while True:
        distance_cm1 = sensor1.distance * 100
        distances.append(distance_cm1)  # Append distance to the list
        sleep(1)
    return distances  # Return the list of distances

distances = dist()  # Call the dist() function and get the list of distances
plt.plot(distances)  # Plot distances
plt.xlabel('Time (seconds)')
plt.ylabel('Distance (cm)')
plt.title('Distance over time')
plt.show()