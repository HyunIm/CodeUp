# File : 1441.py
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
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(*a)
'''
