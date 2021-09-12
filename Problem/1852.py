# File : 1852.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

f = lambda x: str(f(x-1))+' '+str(x) if x>1 else 1
print(f(int(input())))
