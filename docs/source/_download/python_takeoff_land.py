# A simple example to perform a takeoff-lading procedure. 
# The base station (computer running the program) must be connected to the wifi.
#
# Author : S. Delprat

from tello_control import *
import time

# create a tello_control object
drone = tello_control()

# Connect to the drone (assuming the base station is connected to the drone's WIFI)
drone.connect()

# Perform a simple fly
drone.takeoff()
time.sleep(2) # Wait 2 seconds
drone.land()