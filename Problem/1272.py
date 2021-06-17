# File : 1272.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-17
# Brief : 단순 반복문

k, h = map(int, input().split())
k = (k+1)/2 if k%2==1 else k*5
h = (h+1)/2 if h%2==1 else h*5
print(int(k+h))
