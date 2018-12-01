#!/usr/bin/python3
import sys
teams=set()
def points(x):  
    y=[]
    if (x[0]==max(x) and x[0]!=min(x)):
        y=[3,0]
    elif(max(x)!=min(x)):
        y=[0,3]
    else: 
        y=[1,1]
    return y


for line in sys.stdin:
    line=line.strip()
    if len(line)!=0:
        temp=line.split(" ")
        teams=temp[0].split("-")
        result=[int(x) for x in temp[1].split("-")]
        pnt=points(result) 
        for i in range(0,2):
            print("{} {}".format(teams[i], pnt[i]))
