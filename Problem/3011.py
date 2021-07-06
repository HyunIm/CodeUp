# File : 3011.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 데이터 정렬

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

for i in range(n):
    if a==b:
        break
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(i)
