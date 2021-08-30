# File : 1672.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

n, k = map(int, input().split())
if n//k > 9999:
    print('번호 초과 오류')
else:
    for i in range(n//k):
        s = 'F-%4d'%(i+1)
        print(s.replace(' ','0'))
