# File : 1205.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-14
# Brief : 조건문

a, b = map(float, input().split())
print('%.6f'%max(a+b, b+a, a-b, b-a, a*b, a/b, b/a, a**b, b**a))
