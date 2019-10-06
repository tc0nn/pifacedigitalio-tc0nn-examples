#!/bin/python

import pifacedigitalio, time
pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

def alloff():
  for i in range(8):
    print("Setting channel " + str(i) + " off")
    pfd.output_pins[i].turn_off()

def knight_rider():
  from time import sleep
  for loop in range(10):
     for up in range(8):
         pfd.output_pins[up].toggle()
         sleep(0.075)
         pfd.output_pins[up].toggle()
     for down in range(7,0,-1):
         pfd.output_pins[down].toggle()
         sleep(0.075)
         pfd.output_pins[down].toggle()
     up=0
     down=0


def randomness():
 import random as ra
 from time import sleep
 for x in range(1000):
  r=ra.randrange(8)
  o=ra.randrange(2)
  #pfd.output_pins[r].value=o
  pfd.output_pins[r].toggle()
  print("Set " + str(r) + " to " + str(o))
  sleep(0.01)


knight_rider()

alloff()
print("All done")

