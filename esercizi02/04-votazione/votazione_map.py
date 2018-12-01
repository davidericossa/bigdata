#!/usr/bin/python3
import sys

for riga in sys.stdin:
    riga=riga.strip()
    out = '{} {}'.format(riga, 1)
    print(out)
