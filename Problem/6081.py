# File : 6081.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-05
# Brief : 종합

n = int(input(), 16)

for i in range(1, 0xf + 1):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep = '')
