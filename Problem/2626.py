# File : 2626.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-01
# Brief : 탐색기반설계

n = int(input())
r = 0
for i in range(1, n+1):
    if 2*i<n<=3*i: r+=i-(n-i-1)//2
print(r)
