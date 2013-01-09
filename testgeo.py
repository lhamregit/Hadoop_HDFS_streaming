#!/usr/bin/python

import sys
sys.path.append('./geoip')
import pygeoip
	 
# Load the database once and store it globally in interpreter memory.
GEOIP = pygeoip.Database('/home/training/training_materials/data_science/exercises/lasse_lab/cleanedlogfiles/GeoIP.dat')

print "starting"

file = open("/home/training/training_materials/data_science/exercises/lasse_lab/ip.log", "rb")

print "File opened"

for line in file: 
  ip = line.strip()
  print ip
  info = GEOIP.lookup(ip)
  print info
  if info.country:
    print info.country + "\t" + "1"
