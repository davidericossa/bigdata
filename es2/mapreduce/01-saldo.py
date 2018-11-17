#!/usr/bin/python3
import sys
saldo=0
for riga in sys.stdin:
    riga=riga.strip()
    parti=riga.split(';')
    # recupera importo dalla riga 
    importo=float(parti[1])
    saldo+=importo

print('Saldo finale {:.2f}'.format(saldo))
