# 델타를 이용한 2차 배열 탐색

'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# 정답 : 24
def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    else:
        return False


def calabs(y, x):
    if y-x < 0:
        return  (-1)*(y-x)
    elif y-x > 0:
        return y-x
    else:
        return 0

def myabs(a):
    if a < 0: return -a
    else: return a

arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if iswall(testX, testY) == False:
                # sum += abs(arr[y][x] - arr[testY][testX]) #abs 메소드 사용
                sum += calabs(arr[y][x], arr[testY][testX])
print(f'답: {sum}')