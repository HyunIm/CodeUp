# File : 1860.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

f = lambda x: str(f(x-1))+' '+str(x) if x>1 else str(1)
a = list(map(f, map(int, f(int(input())).split())))
n = lambda i: n(i-1)+'\n'+a[i] if i>0 else a[0]
print(n(len(a)-1))
