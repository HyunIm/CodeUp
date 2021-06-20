# File  : 1382.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 중첩 반복문

a = [['%d'%j+' x %d = '%i+'%2d'%(i*j) for j in range(2, 6)] for i in range(1, 10)]
for i in a:
    for j in i:
        print(j, end='\t')
    print()

