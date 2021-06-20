# File  : 1408.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 문자열

s = input()
for i in s:
    print(chr(ord(i)+2), end='')
print()
for i in s:
    print(chr(ord(i)*7%80+48), end='')
