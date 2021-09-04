# File : 1704.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-04
# Brief : 기초

n = input().split()
print(113-int(n[0][:2]) if int(n[1][0]) < 3 else 13-int(n[0][:2]), 'M' if int(n[1][0])%2 else 'F')
