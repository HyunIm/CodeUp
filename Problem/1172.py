# File : 1172.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

n = list(map(int, input().split()))
n.sort()
print(' '.join(str(i) for i in n))
