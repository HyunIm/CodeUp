# File : 1283.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

a = int(input())
b = input()
c = list(map(int, input().split()))
d = a

for i in c:
    a += a*i/100

e = round(a)-d
print(e)
print('same' if e==0 else 'good' if e>0 else 'bad')
