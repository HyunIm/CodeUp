# File : 6085.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-06
# Brief : 종합

w, h, b = map(int, input().split())
mb = ((w * h * b) / 8) / (2 ** 20)
print('%.2f MB' %mb)
