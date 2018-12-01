#!/usr/bin/python3
import sys
from datetime import datetime as dt
saldo=0
for riga in sys.stdin:
    riga=riga.strip()
    parti=riga.split(';')
    # recupera importo dalla riga
    data=parti[0]
    dd=dt.strptime(data,'%d/%m/%Y')
    if dd.month==5 and dd.year==2018:
      print(riga) 
      importo=float(parti[1])
      saldo+=importo

print('Saldo finale {:.2f}'.format(saldo))
