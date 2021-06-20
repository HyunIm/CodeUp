# File  : 1440.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

n = int(input())
k = list(map(int, input().split()))
for i in range(n):
    print(i+1, ':', sep='', end=' ')
    for j in range(n):
        if i==j:
            continue
        elif k[i]==k[j]:
            print('=', end=' ')
        elif k[i]<k[j]:
            print('<', end=' ')
        else:
            print('>', end=' ')
    print()
