# File : 3004.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 데이터 정렬

import sys
import bisect
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(a)
for i in a:
    print(bisect.bisect(b, i)-1, end=' ')
