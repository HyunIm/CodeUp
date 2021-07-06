# File : 1442.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-06
# Brief : 데이터 정렬

n = int(input())
a = [int(input()) for _ in range(n)]
print(*sorted(a))

'''
n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n-1):
    m = i
    for j in range(i+1, n):
        if a[m] > a[j]:
            m = j
    a[i], a[m] = a[m], a[i]

print(*a)
'''
