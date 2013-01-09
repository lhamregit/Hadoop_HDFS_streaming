#!/usr/bin/python

import datetime
import re
import sys

# For extracting request info from the request.
#p = "^([\\'+\\d.]+) (.{19}) (\\w+) ([\\/+\\w+\\d+\\?+\\=+\\&+\\%+\\.+]+) (\\d+) (\\S+) ([\\w+\\d+\\.+]+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) \\S+ ([\\d.]+) ([\\d.]+).*"
#p = "^([\\'+\\d.]+) (.{19}) (\\w+) ([\\/+\\w+\\d+\\?+\\=+\\&+\\%+\\.+\\;+\\*+\\-+]+) (\\d+) (\\S+) ([\\w+\\d+\\.+]+) ([\\'+\\d.\\S+\\s+]+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) \\S+ ([\\d.]+) ([\\d.]+).*"
p = "^([\\'+\\d.\\S+]+) (.{19}) (\\w+) ([\\/+\\S+]+) (\\d+) (\\S+) ([\\w+\\d+\\.+]+) ([\\'+\\d.\\S+\\s+]+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) \\S+ ([\\d.]+) ([\\d.]+).*"

pattern = re.compile(p)

print "starting"

file = open("/home/training/training_materials/data_science/exercises/lasse_lab/cleanedlogfiles/access_fixed.log", "rb")
#file = open("/home/training/training_materials/data_science/exercises/lasse_lab/cleanedlogfiles/a.log", "rb")

print "File opened"

for line in file:
  res = pattern.match(line)
  if res:
    #print 'Match found: ', res.group()
    r = 9
  else:
    print line
    print "no match"
 
print "done"
