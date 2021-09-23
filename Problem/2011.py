# File : 2011.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-24
# Brief : 중급

a, b = map(int, input().split())
for i in range(a, b+1):
    i = str(i)
    r = i.count('3')+i.count('6')+i.count('9')
    if r: print('K'*r)
    else: print(i)
