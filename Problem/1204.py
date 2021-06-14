# File : 1204.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-14
# Brief : 조건문

n = int(input())
t = 'st' if n%10==1 else 'nd' if n%10==2 else 'rd' if n%10==3 else 'th'
t = 'th' if n//10==1 else t
print(n, t, sep='')
