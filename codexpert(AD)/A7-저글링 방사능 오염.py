import sys
sys.stdin = open("A7_input.txt")

def bfs():
    # 1) 시작점을 큐에 저장(방문 표시)
    q = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append((startx, starty, 3))
    arr[starty][startx] = 0
    while q:
        # 2) 큐에서 데이터 읽기(현재 위치)
        x, y, time = q.pop(0)
        # 3) 사방탐색하면서 연결점(길) 찾아 큐에 저장
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 3-1) 맵의 범위 체크
            if nx < 0 or ny < 0 or nx >= X or ny >= Y : continue    # 맵범위를 벗어나면 스킵
            if arr[ny][nx] != 1 : continue  # 저글링이 아니면 스킵
            # 3-2) 연결점 찾아 큐에 저장(방문 표시)
            q.append((nx, ny, time+1))
            arr[ny][nx] = 0
    # 큐가 빈 상태
    return time


X, Y = map(int, input().split())
arr = []
for i in range(Y):
    arr.append(list(map(int, input())))

cnt = 0
startx, starty = map(int,input().split())
startx -= 1
starty -= 1
sol = bfs()
for i in range(Y):
    for j in range(X):
        if arr[i][j] == 1:
            cnt += 1

print(sol)
print(cnt)