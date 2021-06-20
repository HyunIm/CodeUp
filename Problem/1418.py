# File  : 1418.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 문자열

s = input()
for i in range(len(s)):
    if s[i]=='t':
        print(i+1, end=' ')
