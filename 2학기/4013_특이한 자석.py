import sys
sys.stdin = open("특이한 자석_input.txt")

# 시계 방향 함수
def clockwise(a):
    z = a[:]
    tmp = z.pop()
    z.insert(0, tmp)
    return z

# 반시계 방향 함수
def anticlockwise(a):
    z = a[:]
    tmp = z.pop(0)
    z.append(tmp)
    return z

t = int(input())

for case in range(1,t+1):
    k = int(input())

    gear = []
    for i in range(4):
        gear.append(list(map(int,input().split())))

    # for i in range(4):
    #     print(gear[i])

    for i in range(k):
        n, wise = map(int, input().split())
        # print(n, wise)
        leftcnt = 0
        rightcnt = 0

        # 좌측 돌아가는 기어 개수 check
        if n > 1:
            q = n-1
            while q > 0:
                if gear[q][6] != gear[q - 1][2]:
                    leftcnt += 1
                else:
                    q = -1
                q -= 1
            # print('좌측', end=" ")
            # print(leftcnt)

        # 우측 돌아가는 기어 개수 check
        if n <= 3:
            q = n-1
            while q < 3:
                if gear[q][2] != gear[q + 1][6]:
                    rightcnt += 1
                else:
                    q += 999
                q += 1
            # print('우측', end=" ")
            # print(rightcnt)

        # 입력 기어의 돌아가는 방향이 시계방향일 경우
        if wise == 1:
            # 선택 기어 먼저 돌리기
            gear[n-1] = clockwise(gear[n-1])
            # 좌측 기어 돌리기
            for lc in range(1, leftcnt+1):
                if lc % 2 == 1:
                    gear[n-1-lc] = anticlockwise(gear[n-1-lc])
                else:
                    gear[n-1-lc] = clockwise(gear[n-1-lc])
            # 우측 기어 돌리기
            for rc in range(1, rightcnt+1):
                if rc % 2 == 1:
                    gear[n-1+rc] = anticlockwise(gear[n-1+rc])
                else:
                    gear[n-1+rc] = clockwise(gear[n-1+rc])

        # 입력 기어의 돌아가는 방향이 반시계방향일 경우
        elif wise == -1:
            # 선택 기어 먼저 돌리고
            gear[n-1] = anticlockwise(gear[n-1])
            # 좌측 기어 돌리기
            for lc in range(1, leftcnt+1):
                if lc % 2 == 1:
                    gear[n-1-lc] = clockwise(gear[n-1-lc])
                else:
                    gear[n-1-lc] = anticlockwise(gear[n-1-lc])
            # 우측 기어 돌리기
            for rc in range(1, rightcnt+1):
                if rc % 2 == 1:
                    gear[n-1+rc] = clockwise(gear[n-1+rc])
                else:
                    gear[n-1+rc] = anticlockwise(gear[n-1+rc])


        # for i in range(4):
        #     print(gear[i])

    res = 0
    # 각 기어의 12시 방향 값을 구하고 최종 값을 추출
    for i in range(4):
        res += gear[i][0] * 2**i
    print(f'#{case} {res}')







