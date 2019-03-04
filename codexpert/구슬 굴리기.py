import sys
sys.stdin = open("구슬 굴리기_input.txt")

N, n = list(map(int, input().split()))
a = [[1 for _ in range(N+2)]for _ in range(n+2)]

for i in range(1, n+1):
    a[i] = [1] + list(map(int, input())) + [1]

# for i in range(n+2):
#     print(a[i])

t = int(input())
b = list(map(int, input().split()))

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

xi = 0
yi = 0
dindex = 0
cnt = 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            yi = i
            xi = j
# print(yi, xi)

while True:

    # 가던 진행방향으로 1칸 이동하여 좌표 계산
    xi += dx[b[dindex]]
    yi += dy[b[dindex]]

    # 현위치가 0이면 카운트, 방문표시
    if a[yi][xi] == 0:
        a[yi][xi] = 3
        cnt += 1

    # 현위치가 1이면 이전좌표로 재이동, 다음방향증가
    elif a[yi][xi] == 1:
        xi -= dx[b[dindex]]
        yi -= dy[b[dindex]]
        dindex += 1
        if dindex == t:
            break


# print(dindex)
# for i in range(n+2):
#     print(a[i])

print(cnt)

