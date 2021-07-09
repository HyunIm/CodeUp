# File : 3702.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

m = {}
def f(x, y):
    if x==1 or y==1: return 1
    if (x,y) in m: return m[(x,y)]
    else: m[(x,y)] = f(x-1, y)+f(x, y-1); return m[(x,y)]
r, c= map(int, input().split())
print(f(r, c)%100000000)
