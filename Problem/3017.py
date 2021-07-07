# File : 3017.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 데이터 정렬

n = int(input())
s = [[i] for i in range(1, n+1)]
for i in range(n):
    s[i] = s[i]+list(map(int, input().split()))
s.sort(key=lambda x: (-x[1], -x[2], x[0]))
for i in s:
    print(*i)
