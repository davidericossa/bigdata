#!/usr/bin/python3

import sys
name=" "
for line in sys.stdin:
	if name==line.strip() and name!="":
		count=count+1	
	else:
		if name!=" " and name!="":
			print("{} {}".format(name, count))		
		count=1
		name=line.strip()
print("{} {}".format(name, count))
		
