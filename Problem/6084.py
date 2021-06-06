# File : 6084.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-06
# Brief : 종합

h, b, c, s = map(int, input().split())
mb = ((h * b * c * s) / 8) / (2 ** 20)
print('%.1f MB' %mb)
