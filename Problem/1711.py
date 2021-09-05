# File : 1711.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-05
# Brief : 기초

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print('충돌' if x1<=x3<=x2 and y1<=y3<=y2 else '비충돌')
