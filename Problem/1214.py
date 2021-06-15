# File : 1214.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-15
# Brief : 조건문

y, m = map(int, input().split())
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(29 if ((y%400==0) or (y%4==0 and y%100!=0)) else d[m-1])
