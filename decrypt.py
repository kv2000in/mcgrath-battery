#!/usr/bin/python
import sys
myreadfile = open(sys.argv[1],'r')
for eachline in myreadfile:
	mydisplayednumberonscreen = eachline.split(",")[0]
	myhexread = eachline.split(",")[1]
	myindividualhexs = myhexread.split(" ")
	print(mydisplayednumberonscreen)
	#print(myhexread)
	#print(myindividualhexs)
	# format seems to be [F4,02,00,03,MM,00,SS,00]
	# displayednumber = 250-MM
	#F4 decreases by 3 every minute. No change otherwise. 02 and 03 and 00 spaces haven't changed
	print([int(x,16) for x in myindividualhexs])
	

