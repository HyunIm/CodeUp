# File : 2002.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-19
# Brief : 중급

k = int(input())
n = input()
for i in range(len(n)):
    c = ord(n[i])-(3*(i+1)+k)
    print(chr(c) if c>64 else chr(c+26), end='')
