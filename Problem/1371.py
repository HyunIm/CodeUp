# File  : 1371.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 중첩 반복문

n = int(input())
for i in range(n):
    print(' '*(n-i-1)+'*'+' '*(i*2)+'*')
for i in range(n, 0, -1):
    print(' '*(n-i)+'*'+' '*((i-1)*2)+'*')
