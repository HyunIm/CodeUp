# File : 2001.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-23
# Brief : 그리디

n = [int(input()) for _ in range(5)]
r = min(n[0:3])+min(n[3:5])
print(r+r/10)
