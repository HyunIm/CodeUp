# File : 1859.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

f = lambda x: f(x-1)+'*'*x+'\n' if x>1 else '*\n'
print(f(int(input())))
