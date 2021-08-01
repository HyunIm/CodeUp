# File : 2625.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-01
# Brief : 탐색기반설계

n = int(input())
r = 0
for a in range(1, n//3+1):
    for b in range((n-a)//2, a-1, -1):
        c = n-a-b
        if a+b>c: r += 1
        else: break
print(r)
