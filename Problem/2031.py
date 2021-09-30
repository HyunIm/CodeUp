# File : 2031.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-27
# Brief : 중급

n = input()
r = 0
t = 1
for i in n[::-1]:
    r += (ord(i)-64) * t
    t *= 26
print(r)
