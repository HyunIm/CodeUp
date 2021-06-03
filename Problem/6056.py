# File : 6056.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-03
# Brief : 연산

a, b = map(bool, map(int, input().split()))
print(((not a) and b) or ((not b) and a))
