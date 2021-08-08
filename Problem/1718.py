# File : 1718.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-08
# Brief : 출력

print((lambda x:(int(x[0][1:])*12 if x[0][1:] else 12)+(int(x[1]) if x[1] else 1))(input().split(sep='H')))
