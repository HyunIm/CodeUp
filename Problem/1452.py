# File : 1452.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-06
# Brief : 데이터 정렬

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
print(*sorted(a))
