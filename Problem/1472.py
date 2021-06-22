# File : 1472.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-22
# Brief : 2차원 배열

n, m = map(int, input().split())
for i in range(n-1, -1, -1):
    for j in range(m, 0, -1):
        print(i*m+m-j+1 if i%2 else i*m+j, end=' ')
    print()
