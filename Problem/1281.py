# File : 1281.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

a, b = map(int, input().split())
n = [i if i%2==1 else -i for i in range(a, b+1)]
f = 0
for i in n:
    if f==0:
        print(i, end='')
    else:
        print('%+d'%i, end='')
    f += 1
print('=', sum(n), sep='')
