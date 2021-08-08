# File : 1174.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-08
# Brief : 기초

h, m = map(int, input().split())
t = h*60+m-30+60*24
print(int(t/60%24), (t%60))
