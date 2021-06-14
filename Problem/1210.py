# File : 1210.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-14
# Brief : 조건문

a, b = map(int, input().split())
d = (0, 400, 340, 170, 100, 70)
print('angry' if d[a]+d[b]>500 else 'no angry')
