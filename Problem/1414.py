# File  : 1414.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 문자열

s = input().lower()
cnt = 0
print(s.count('c'))
for i in range(len(s)):
    if s[i:i+2]=='cc':
        cnt += 1
print(cnt)
