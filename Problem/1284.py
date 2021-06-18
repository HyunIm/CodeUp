# File : 1284.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

n = int(input())
for i in range(2, n):
    d = n / i
    if d%1 == 0:
        a = [j for j in range(2, int(d)) if d%j==0]
        if not a:
            a = [k for k in range(2, i) if i%k==0]
            if not a:
                break
            else:
                continue
        else:
            continue

if n==1 or n==2 or i==n-1:
    print('wrong number')
else:
    print(i, int(d))
