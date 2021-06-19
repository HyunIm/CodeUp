# File  : 1356.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

n = int(input())
print('*'*n)
for i in range(n-2):
    print('*'+' '*(n-2)+'*')
print('*'*n)
