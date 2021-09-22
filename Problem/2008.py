# File : 2008.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-22
# Brief : 중급

n = input()
a = list(map(int, input().split()))
if a[0] == a[-1]: print('섞임')
elif a == sorted(a): print('오름차순')
elif a == sorted(a, reverse=True): print('내림차순')
else: print('섞임')
