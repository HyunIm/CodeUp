# File  : 1430.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

# 메모리 초과 (실패)
# 메모리 : 196632 or 808972
# 시간 : 12 or 221

'''
n = input()
a = input().split()
m = input()
b = input().split()

for i in b:
    if i in a:
        print('1', end=' ')
    else:
        print('0', end=' ')
'''

'''
n = int(input())
a = [0]*100000001
i = list(map(int, input().split()))
for j in range(n):
    a[i[j]] = 1

m = int(input())
i = list(map(int, input().split()))
for j in range(m):
    print(a[i[j]], end=' ')
'''

'''
n = int(input())
i = list(map(int, input().split()))
a = [0]*(max(i)+1)
for j in range(n):
    a[i[j]] = 1

m = int(input())
i = list(map(int, input().split()))

if len(a) <= max(i):
    for _ in range(max(i)-len(a)+2):
        a.append(0)

for j in range(m):
    print(a[i[j]], end=' ')
'''

'''
n = int(input())
a = {}
i = list(map(int, input().split()))
for j in range(n):
    a[i[j]] = 1

m = int(input())
i = list(map(int, input().split()))
for j in range(m):
    try:
        print(a[i[j]], end=' ')
    except KeyError:
        print(0, end=' ')
'''

'''
n = input()
a = input().split()
m = input()
b = input().split()

for i in b:
    if a.count(i):
        print('1', end=' ')
    else:
        print('0', end=' ')
'''

'''
import sys

n = int(input())
a = {}
i = list(map(int, sys.stdin.readline().split()))
for j in range(n):
    a[i[j]] = 1

m = int(input())
i = list(map(int, sys.stdin.readline().split()))
for j in range(m):
    try:
        print(a[i[j]], end=' ')
    except KeyError:
        print(0, end=' ')
'''
