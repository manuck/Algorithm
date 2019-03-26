import sys
sys.stdin = open("B0_input.txt")

def bfs():
    global starty, startx, n
    # 1) 시작점을 큐에 저장(방문 표시)
    q = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append((startx, starty))
    arr[starty][startx] = 0
    cnt = 1
    while q:
        # 2) 큐에서 데이터 읽기(현재 위치)
        x, y = q.pop(0)
        # 3) 사방탐색하면서 연결점(길) 찾아 큐에 저장
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 3-1) 맵의 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 맵범위를 벗어나면 스킵
                continue
            if arr[ny][nx] != 1:    # 단지가 아니면 스킵
                continue
            # 3-2) 연결점 찾아 큐에 저장(방문 표시)
            q.append((nx, ny))
            arr[ny][nx] = 0
            cnt += 1
    # 큐가 빈 상태
    return cnt

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

res = []
while True:
    flag = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                flag = 1
                startx = j
                starty = i

    if flag == 0:
        break
    else:
        res.append(bfs())

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])



