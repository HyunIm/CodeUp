# File : 1760.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

a = input()
b = input()
c = {' ':' '}
for i, j in enumerate(a): c[j] = i
for i in b: print(c[i], end='')
