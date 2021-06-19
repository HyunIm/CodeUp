# File  : 1355.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

n = int(input())
a = [' '*(n-i)+'*'*i for i in range(n, 0, -1)]
for i in a:
    print(i)
