#!/usr/bin/python3
import sys
voti=0
candidato=None

for riga in sys.stdin:
    nome=riga.split()[0]
    if candidato==None:
        candidato=nome
        voti=1
    elif candidato==nome:
        voti+=1
    else:
        out = '{} {}'.format(candidato, voti)
        print(out)
        candidato=nome
        voti=1
out = '{} {}'.format(candidato, voti)
print(out)


