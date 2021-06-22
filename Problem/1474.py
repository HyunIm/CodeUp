# File : 1474.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-22
# Brief : 2차원 배열

n, m = map(int, input().split())
for i in range(n, 0, -1):
    for j in range(m-1, -1, -1):
        print(n-i+j*n+1 if j%2 else i+j*n, end=' ')
    print()
