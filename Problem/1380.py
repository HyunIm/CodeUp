# File  : 1380.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 중첩 반복문

k = int(input())
for i in range(1, 7):
    for j in range(1, 7):
        if i+j==k:
            print(i, j)
