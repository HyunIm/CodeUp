# File : 1579.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

mymax = lambda x, y: x if x<y else y
a, b= map(int, input().split())
print(mymax(a, b))
