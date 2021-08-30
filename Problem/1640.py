# File : 1640.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

r = 0
for _ in range(int(input())):
    p = input()
    if len(p) < 4: print(p); r+=1
    elif 'tap' in p: print(p); r+=1
    elif 'xocure' in p: print(p); r+=1
print('safe' if 0<=r<4 else 'warning' if 3<r<7 else 'danger')
