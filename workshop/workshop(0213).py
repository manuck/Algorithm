import sys
sys.stdin = open("0213_input.txt")

for case in range(10):
    n = int(input())
    a = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        a[i] = list(map(int, input().split()))

    y = 99
    x = 0
    res = 0

    # 도착지점 찾기
    for i in range(100):
        if a[y][x] == 2:
            y -= 1
            break
        else:
            x += 1

    while y != 0:
        #  없으면 위로
        if a[y - 1][x] == 1:
            y -= 1

        # 우측 확인
        if x != 99 and a[y][x + 1] == 1:
            for i in range(99 - x):
                if a[y][x + i] == 0:
                    x += (i - 1)
                    break
                elif x + i == 98:
                    x = 99
                    break
        # 좌측 확인
        elif x != 0 and a[y][x - 1] == 1:
            for j in range(x):
                if a[y][x - j] == 0:
                    x -= (j - 1)
                    break
                elif x - j == 0:
                    x = 0
                    break

        if y == 0:
            res = x

    print(f'#{case + 1} {res}')