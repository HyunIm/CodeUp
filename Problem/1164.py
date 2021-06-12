# File : 1164.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

n = list(map(int, input().split()))
print('CRASH' if min(n)<=170 else 'PASS')
