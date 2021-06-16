# File : 1254.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

a, z = input().split()
for i in range(ord(z)-ord(a)+1):
    print(chr(ord(a)+i), end=' ')
