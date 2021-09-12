# File : 1853.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

f = lambda x: x+f(x-1) if x>1 else 1
print(f(int(input())))
