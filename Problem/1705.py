# File : 1705.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-04
# Brief : 기초

s = input()
n = s.count('3')+s.count('6')+s.count('9')
print(s if n==0 else 'K' if n==1 else 'KK' if n==2 else 'KKK')
