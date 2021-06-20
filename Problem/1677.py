# File  : 1677.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 중첩 반복문

n, m = map(int, input().split())
print('+'+'-'*(n-2)+'+')
for _ in range(m-2):
    print('|'+' '*(n-2)+'|')
print('+'+'-'*(n-2)+'+')
