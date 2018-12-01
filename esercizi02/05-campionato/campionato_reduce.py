#!/usr/bin/python3
import sys
totale_punti=0
squadra_corrente=None

for riga in sys.stdin:
    squadra, punti=riga.split()
    punti=int(punti)
    if squadra_corrente==None:
        squadra_corrente=squadra
        totale_punti=punti
    elif squadra_corrente==squadra:
        totale_punti+=punti
    else:
        out = '{} {}'.format(squadra_corrente, totale_punti)
        print(out)
        squadra_corrente=squadra
        totale_punti=punti
out = '{} {}'.format(squadra_corrente, totale_punti)
print(out)
