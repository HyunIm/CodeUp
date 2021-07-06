# File : 1443.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-06
# Brief : 데이터 정렬

n = int(input())
a = [int(input()) for _ in range(n)]
print(*sorted(a))

'''
n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(1, n):
    j = i-1
    k = a[i]
    while a[j]>k and j>=0:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = k

print(*a)
'''
