#!/usr/bin/python3
import sys

for riga in sys.stdin:
    riga=riga.strip()
    if len(riga)<1:
        continue
    squadre, goal = riga.split()
    squadraCasa, squadraOspite = squadre.split('-')
    goalCasa, goalOspite = goal.split('-')
    if goalCasa==goalOspite:
        print('{} {}'.format(squadraCasa, 1))
        print('{} {}'.format(squadraOspite, 1))
    elif goalCasa>goalOspite:
        print('{} {}'.format(squadraCasa, 3))
    else:
        print('{} {}'.format(squadraOspite, 3))
