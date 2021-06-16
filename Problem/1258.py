# File : 1258.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

n = int(input())
print(int((n/2)*(n/2)) if n%2==1 else int((n/2)*(n/2)+(n/2)))
