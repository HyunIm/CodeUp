# File : 1617.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

n = input()
s = str(int(n)+int(n[::-1]))
print('YES' if s==s[::-1] else 'NO')
