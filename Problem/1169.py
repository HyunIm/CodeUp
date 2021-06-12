# File : 1169.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

n = int(input())
y = 113-n if 113-n<100 else 13-n
g = 1 if 113-n<100 else 3
print(y, g)
