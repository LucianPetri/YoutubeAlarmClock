# 	Project made by Petri Lucian - Emanuel 
#	Email: petri.lucian@outlook.com

#	start date of the project 		---> 8 December 2016
#	end date of the project 		---> 9 December 2016

"""
Project Objectives:
	== Create an alarm with the following proprieties:
		- read a file named youtube.txt
		- after setting the alarm time, when the alarm goes off start a random youtube video from the youtube text file
"""
"""
Stackoverflow links that helped:

==	http://stackoverflow.com/questions/10978869/safely-create-a-file-if-and-only-if-it-does-not-exist-with-python
==	http://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list-with-python

"""

import time
import webbrowser 
import random
import os

#	checking if the file exists
if 	os.path.isfile("youtube.txt") == False:
	
	print 	"\nError the file youtube.txt is missing.   Creating default file...\n"

	#	originally there should have been a stop here but I added so that if the youtube.txt dosent exist
	#	it auto adds a default youtube.txt file with 3 links
	flags			=	os.O_CREAT | os.O_EXCL | os.O_WRONLY 
	CreatedFile 	= 	os.open("youtube.txt", flags)

	with os.fdopen(CreatedFile, 'w') as CreatedFile:
	   CreatedFile.write("https://www.youtube.com/watch?v=2YllipGl2Is")
	   CreatedFile.write("https://www.youtube.com/watch?v=zrP6nx2Pm5U")
	   CreatedFile.write("https://www.youtube.com/watch?v=6sYGMaACz_k")


print 	"\nAt what hour would you like to wake up?\n"
print	"please use the format: 00:00 - 23:59	example: 13:24\n"

# Variable for the Alarm
Alarm 	=	raw_input(">> ")

# 	Variable for the time to use in the while loop
Time 	=	time.strftime("%H:%M")

# Opening the file
with open("youtube.txt") as YoutubeFile:

	content	=	YoutubeFile.readlines()

# refreshing the time variable for accurate time
while Time != Alarm:
	
	Time 	= 	time.strftime("%H:%M")

# If the time is equal to the Alarm we've setup then active the base code
if Time == Alarm:
	
	print "Wake up!!"

# Variable for the random video in the text file
	Video		= 	random.choice(content)

# opens the youtube link in a new tab if available if not then in a new window
	webbrowser.open_new_tab(Video)

# closes the file so it wont stay in the process
os.close("youtube.txt")