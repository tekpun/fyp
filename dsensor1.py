from gpiozero import DistanceSensor
from time import sleep

def dist():
	sensor1 = DistanceSensor(echo=18, trigger=17)
	while True:
		distance_cm1 = sensor1.distance * 100
		sleep(1)
	GPIO.cleanup()
dist()
distance = dist.distance_cm1
print(distance)
