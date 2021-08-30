# File : 1671.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

a, b = map(int, input().split())
print('tie' if a==b else 'win' if (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0) else 'lose')
