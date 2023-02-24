#!/usr/bin/env python

rec = input('unesi rec: ')
duzina = len(rec)

i = 1
j = ''
for i in range(duzina):
    a = rec[-i]
    i = i + i
    j = j + a

print(j[1:] + j[0])
