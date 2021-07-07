# File : 4701.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 데이터 정렬

n = int(input())
a = sorted(list(map(int, input().split())))
x, y, i, j = 0, n-1, 0, n-1

r = abs(a[i]+a[j])
while i<j and r:
    t = a[i]+a[j]
    if abs(t) < r:
        x = i; y = j; r = abs(t)
    if t>0: j-=1
    else: i+=1

print(a[x], a[y])
