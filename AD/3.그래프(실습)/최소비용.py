import sys
sys.stdin = open("최소비용_input.txt")

'''
출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

(표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)
 
0   2   1

0   1   1

1   1   1

인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.
 
0   2   1

0   1   1

1   1   1

색이 칠해진 칸을 따라 이동하는 경우 기본적인 연료 소비량 4에, 높이가 0에서 1로 경우만큼 추가 연료가 소비되므로 최소 연료 소비량 5로 목적지에 도착할 수 있다.

이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.

1<=T<=50, 3<=N<=100, 0<=H<1000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
'''

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = []
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            h = 0
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if arr[ny][nx] > arr[y][x]:
                h = arr[ny][nx] - arr[y][x]
            # 가볼위치의 이전의 해 > 현재진행경로의 해 비교하여 최소이면
            if visited[ny][nx] > visited[y][x] + 1 + h :
                q.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1 + h

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [[0 for _ in range(n)]for _ in range(n)]
    visited = [[10000000 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    # print(arr)
    bfs()
    print('#%i ' % (case), end="")
    print(visited[n-1][n-1])

