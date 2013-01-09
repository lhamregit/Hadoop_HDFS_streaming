#!/usr/bin/python
import sys
import re
sys.path.append('./geoip')
import pygeoip
	 
# create the match criteria
p = "^([\\'+\\d.\\S+]+) (.{19}) (\\w+) ([\\/+\\S+]+) (\\d+) (\\S+) ([\\w+\\d+\\.+]+) ([\\'+\\d.\\S+\\s+]+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) \\S+ ([\\d.]+) ([\\d.]+).*"
pattern = re.compile(p)

# Load the database once and store it globally in interpreter memory.
GEOIP = pygeoip.Database('geoip/GeoLiteCity.dat')

for line in sys.stdin:
  res = pattern.match(line)
  if res:
    ip = res.group(1)
    if ip!= "-":
      info = GEOIP.lookup(res.group(1))
      newline = res.group() + ' ' +  str(info.city)
      print newline.strip()
  else:
    print line + ' ' +  'NYE'
