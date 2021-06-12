# File : 1173.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

h, m = map(int, input().split())
print(h if m>=30 else h-1 if h!=0 else 23, m-30 if m>=30 else m+30)
