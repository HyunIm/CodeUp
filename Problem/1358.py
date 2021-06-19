# File  : 1358.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

n = int(input())
j = n//2
for i in range(1, n+1, 2):
    print(' '*j, end='')
    print('*'*i)
    j -= 1
