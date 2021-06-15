# File : 1216.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-15
# Brief : 조건문

a, b, c = map(int, input().split())
print('advertise' if a<b-c else 'do not advertise' if a>b-c else 'does not matter')
