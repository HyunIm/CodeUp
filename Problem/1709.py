# File : 1709.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-06
# Brief : 데이터 정렬

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)
