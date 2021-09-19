# File : 1954.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-19
# Brief : 기초

f = lambda x: '*'*x+'\n'+f(x-1) if x>1 else '*'
n = int(input())
print(f(n))
