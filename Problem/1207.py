# File : 1207.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-14
# Brief : 조건문

a = list(map(int, input().split()))
d = ('모', '도', '개', '걸', '윷')
print(d[sum(a)])
