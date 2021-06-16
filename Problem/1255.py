# File : 1255.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

a, b = map(float, input().split())
for i in range(int(round(100*a)), int(round(100*b))+1):
    if i/100 != 0:
        print('%.2f'%(i/100), end=' ')
    else:
        print('-0.00', end=' ')
