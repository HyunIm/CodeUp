# File  : 2721.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 문자열

a = input()
b = input()
c = input()
print('good' if (a[-1]==b[0] and b[-1]==c[0] and c[-1]==a[0]) else 'bad')
