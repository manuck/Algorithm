import sys
sys.stdin = open("D4_input.txt")

# 동쪽 = 1 , 서쪽 = 2 , 남쪽 = 3 , 북쪽 = 4


def bfs():
    dx = []
    dy = []

m, n = map(int, input().split())    # m 세로 , n 가로
arr = [[0 for _ in range(n)]for _ in range(m)]
for i in range(m):
    arr[i] = list(map(int, input().split()))
    print(arr[i])

sy, sx, sd = list(map(int, input().split())) # 출발 지점 좌표와 방향
ey, ex, ed = list(map(int, input().split()))   # 도착 지점 좌표와 방향
print(sy, sx)
print(ey, ex)

