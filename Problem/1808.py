# File : 1808.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

n = input()
for i in n:
    if i=='H':
        print('Hello, world!', end=' ')
    elif i=='Q':
        print(n, end=' ')
    elif i=='9':
        for i in range(99, 2, -1):
            print(i, 'bottles of beer on the wall,', i, 'bottles of beer. ')
            print('Take one down and pass it around,', i-1, 'bottles of beer on the wall. ')
        print('2 bottles of beer on the wall, 2 bottles of beer. ')
        print('Take one down and pass it around, 1 bottle of beer on the wall. ')
        print('1 bottle of beer on the wall, 1 bottle of beer. ')
        print('Take one down and pass it around, no more bottles of beer on the wall. ')
        print('No more bottles of beer on the wall, no more bottles of beer. ')
        print('Go to the store and buy some more, 99 bottles of beer on the wall.', end=' ')
