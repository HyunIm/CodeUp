# File : 1229.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 조건문

h, w = map(float, input().split())
s = h-100 if h<150 else (h-100)*0.9 if h>=160 else (h-150)/2+50
o = (w-s)*100/s
print('정상' if o<=10 else '비만' if o>20 else '과체중')
