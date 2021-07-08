# File : 3015.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n, m = map(int, input().split())
s = sorted([list(input().split()) for _ in range(n)], key=lambda x:int(x[1]), reverse=True)
for i in range(m):
    print(s[i][0])
