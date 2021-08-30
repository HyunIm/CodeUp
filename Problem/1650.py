# File : 1650.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

w, h = map(int, input().split())
a = [' ****  ***  ***   ***** *   * ****',
    '*     *   * *  *  *     *   * *   *',
    '*     *   * *   * *     *   * *   *',
    '*     *   * *   * ****  *   * ****',
    '*     *   * *   * *     *   * *',
    '*     *   * *  *  *     *   * *',
    ' ****  ***  ***   *****  ***  *']
for i in a:
    for y in range(h):
        for j in i:
            for x in range(w):
                print(j, end='')
        print()
