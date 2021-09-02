# File : 1702.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-03
# Brief : 기초

a = list(map(int, input().split()))
if a[1]%2: print(*a, sep='')
else: print(*a, sep='', end=' '); print(*a, sep='')
