# File  : 1412.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

s = input()
for i in range(ord('a'), ord('z')+1):
    print(chr(i), ':', s.count(chr(i)), sep='')
