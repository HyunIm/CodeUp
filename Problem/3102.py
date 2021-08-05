# File : 3102.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-04
# Brief : 스택

n = int(input())
s = []
for i in range(n):
    c = input()
    if c[:3]=='pus': s.append(int(c[6:-1]))
    elif c[:3]=='top': print(s[-1] if s else -1)
    elif c[:3]=='pop': s.pop() if s else 0
    elif c[:3]=='siz': print(len(s))
    else: print('false' if s else 'true')