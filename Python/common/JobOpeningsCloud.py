# JobOpeningsCloud.py
#
# To compile gamasutra jobs newsletter into a word cloud of job positions with no. of occurences.

import os

newsletterPath = "d:\\trash"
newsletterFilename = "Gmail - Gamasutra Jobs Newsletter -Week of September 15, 2014.htm"

newsletterFile = os.path.join(newsletterPath, newsletterFilename)

f = open(newsletterFile, 'r')

lines = f.readlines()

for line in lines:
	if line.startswith("<li"):
		tokens = line.split(">")
		subtokens = tokens[2].split("<")
		if "artist" in subtokens[0].lower():
			print subtokens[0]
