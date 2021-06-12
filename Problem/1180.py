# File : 1180.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

n = int(input())
r = (n%10*10 + n//10) * 2 if (n%10*10 + n//10) * 2 < 100 else (n%10*10 + n//10) * 2 % 100
print(r)
print('GOOD' if r<=50 else 'OH MY GOD')
