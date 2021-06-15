# File : 1212.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-15
# Brief : 조건문

n = list(map(int, input().split()))
print('yes' if max(n)<sum(n)-max(n) else 'no')
