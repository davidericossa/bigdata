#!/usr/bin/python3
import sys
totale_categoria=0
ultima_categoria=None

for riga in sys.stdin:
    riga=riga.strip()
    parti=riga.split()
    importo=float(parti[1])
    categoria=parti[0]
    if ultima_categoria==None:
      totale_categoria=importo
      ultima_categoria=categoria
    elif ultima_categoria==categoria:
      totale_categoria+=importo
    else:
      print('{}\t{}'.format(ultima_categoria, totale_categoria))
      totale_categoria=importo
      ultima_categoria=categoria
print('{}\t{}'.format(ultima_categoria, totale_categoria))
