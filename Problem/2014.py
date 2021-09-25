# File : 2014.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-25
# Brief : 중급

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if (100*i+10*j+k) - (10*i+j) == (10*k+k):
                print(i,j,k,'-',i,j,'=',k,k, sep='')
