#!/usr/bin/env python3
#from es1 import *
# wordsfrequencies()
# metti chmode a+x main.py
# esegui con cat talesOfTwoCities.txt | ./main

import sys

sys.stdout.write('start \n')
#sys.stdout.write(sys.stdin.readline())

parole={}
stripping={',', '\n', ''}

for line in sys.stdin:
	temp=line.split(' ')	
	for words in temp:
		for punctuation in stripping:
			temp=temp.strip(punctuation)
		
print()	


sys.stdout.write('end \n')
