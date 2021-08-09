# File : 1289.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-09
# Brief : 기초

n = [list(map(int, input().split())) for _ in range(3)]
print(max(n[0][0]*n[0][1], n[1][0]*n[1][1], n[2][0]*n[2][1]))
