import sys
sys.stdin = open("달팽이사각형_input.txt")

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

n = int(input())
result_list = [[0 for _ in range(n)] for _ in range(n)]
mylist=list(range(1,n+1))


for i in range(n):
    for j in range(n):
        mylist[i].append(j)
result_list[0][0] = my_min(mylist)

for i in range(n+1):
    for j in range(n+1):
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