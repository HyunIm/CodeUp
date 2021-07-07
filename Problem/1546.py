# File : 1546.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

zero = lambda x: not bool(x)
plus = lambda x: True if x>0 else False
n = int(input())
print('zero' if zero(n) else 'plus' if plus(n) else 'minus')
