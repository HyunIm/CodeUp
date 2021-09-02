# File : 1679.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-02
# Brief : 기초

n = int(input())
f = True
for i in range(1, n//3+1):
    for j in range(i, n//2+1):
        k = n - i - j
        if k < i+j and k == max(i, j, k):
            print(i, j, k)
            f = False
if f: print(-1)
