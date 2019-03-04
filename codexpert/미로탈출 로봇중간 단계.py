import sys
sys.stdin = open("미로탈출 로봇중간 단계_input.txt")

n = int(input())
a = [[1 for _ in range(n+2)]for _ in range(n+2)]
for i in range(1, n+1):
    a[i] = [1] + list(map(int, input())) + [1]
b = list(map(int, input().split()))
# for i in range(n+2):
#     print(a[i])
# print(b)
# print()
dy = [0, 1, 0, -1, 0]
dx = [0, 0, -1, 0, 1]
#
dindex = 0
xi = 1
yi = 1
cnt = 0

while True:

    # 가던 진행방향으로 1칸 이동하여 좌표 계산
    xi += dx[b[dindex]]
    yi += dy[b[dindex]]

    # 현위치가 0이면 카운트, 방문표시
    if a[yi][xi] == 0:
        a[yi][xi] = 2
        cnt += 1

    # 현위치가 1이면 이전좌표로 재이동, 다음방향증가
    elif a[yi][xi] == 1:
        xi -= dx[b[dindex]]
        yi -= dy[b[dindex]]
        dindex += 1
        if dindex == 4:
            dindex=0

    # 현위치가 2이면 방문한 자리이므로 탈출
    elif a[yi][xi] == 2:
        break

# print(dindex)
# for i in range(n+2):
#     print(a[i])

print(cnt)

