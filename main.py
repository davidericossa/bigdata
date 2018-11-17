#!/usr/bin/env python3
#from es1 import *
# wordsfrequencies()
# metti chmode a+x main.py
# esegui con cat talesOfTwoCities.txt | ./main

import sys, nltk, textblob
from nltk.corpus import stopwords

sys.stdout.write('start \n')
#sys.stdout.write(sys.stdin.readline())

wordsinstances={}

for line in sys.stdin:
	blob=textblob.TextBlob(line)
	lowerwords=[x.lower() for x in blob.words]
	filtered=list(filter(lambda x: not x in stopwords.words('english'), lowerwords))
	keys=set(wordsinstances.keys()).union(set(filtered))	
	values=[wordsinstances[key]+filtered.count(key) if key in wordsinstances.keys() else filtered.count(key) for key in keys]
	wordsinstances=dict(zip(keys,values))


print (wordsinstances)
sys.stdout.write('end \n')
