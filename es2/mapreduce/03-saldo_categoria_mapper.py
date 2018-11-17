#!/usr/bin/python3
import sys

for riga in sys.stdin:
    riga=riga.strip()
    parti=riga.split(';')
    importo=float(parti[1])
    categoria=parti[2]
    print('{}\t{}'.format(categoria, importo))
