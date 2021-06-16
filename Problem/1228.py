# File : 1228.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 조건문

a, b = map(float, input().split())
c = (a-100)*0.9
d = (b-c)*100/c
print('정상' if d<=10 else '비만' if d>20 else '과체중')
