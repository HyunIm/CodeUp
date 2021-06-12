# File : 1168.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

y, s = map(int, input().split())
print(13 - (y//10000) if s==3 or s==4 else 113 - (y//10000))
