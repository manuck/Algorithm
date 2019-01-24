'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''

mylist = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
result_list = [[0 for _ in range(5)] for _ in range(5)]

def iswall(x, y):
    if x >= 0 and x < 5 and y >= 0 and y < 5 and result_list[x][y] == 0:
        return True
    else:
        return False

def my_min(a):
    mymin = 99
    min_X = 0
    min_Y = 0
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] < mymin:
                mymin = a[x][y]
                min_X, min_Y = x, y
    a[min_X][min_Y] = 99
    return mymin

minx = 0
miny = 0
cnt = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


result_list[0][0] = my_min(mylist)

for i in range(6):
    for j in range(6):
        minx += dx[cnt%4]
        miny += dy[cnt%4]

        if iswall(minx, miny) == True:
            result_list[minx][miny] = my_min(mylist)
            freex=minx
            freey=miny
        elif iswall(minx, miny) == False:
            cnt += 1
            minx=freex
            miny=freey
print(result_list)