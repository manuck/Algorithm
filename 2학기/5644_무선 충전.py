import sys
sys.stdin = open("무선 충전_input.txt")


def check():
    global ax, ay, bx, by
    maplist[ay][ax]



t = int(input())

for case in range(1,t+1):
    maplist = [[0 for _ in range(10)] for _ in range(10)]

    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # print(m, n)
    # print(a)
    # print(b)
    for i in range(n):
        apx, apy, c, power = map(int, input().split())
        apx -= 1
        apy -= 1
        # print(apx, apy, c, power)
        tmp = 0
        for j in range(apy, apy-c-1, -1):
            if j < 0 or j >= 10:
                break
            for q in range(apx-c+tmp, apx+c-tmp+1):
                if q < 0 or q >= 10:
                    continue
                elif maplist[j][q] < power:
                    maplist[j][q] = power
            tmp += 1

        tmp2 = 0
        for j in range(apy, apy+c+1):
            if j < 0 or j >= 10:
                break
            for q in range(apx-c+tmp2, apx+c-tmp2+1):
                if q < 0 or q >= 10:
                    continue
                elif maplist[j][q] < power:
                    maplist[j][q] = power
            tmp2 += 1

    # for i in range(10):
        # print(maplist[i])

    ax, ay = 0, 0
    bx, by = 9, 9
    sola, solb = 0, 0
    sola += maplist[ay][ax]
    solb += maplist[by][bx]
    for i in range(m):
        # print(a[i])
        # print(ax, ay)
        # print(maplist[ay][ax])
        if a[i] == 0:
            # print('제자리')
            continue
        elif a[i] == 1 and ay > 0:
            # print('위로')
            ay -= 1
        elif a[i] == 2 and ax < 9:
            # print('우로')
            ax += 1
        elif a[i] == 3 and ay < 9:
            # print('아래로')
            ay += 1
        elif a[i] == 4 and ax > 0:
            # print('좌로')
            ax -= 1

        if b[i] == 0:
            continue
        elif b[i] == 1 and by > 0:
            by -= 1
        elif b[i] == 2 and bx < 9:
            bx += 1
        elif b[i] == 3 and by < 9:
            by += 1
        elif b[i] == 4 and by > 0:
            bx -= 1
        # print(ax, ay)
        if maplist[ay][ax] == maplist[by][bx] and maplist[ay][ax] != 0:
            bctmp = maplist[ay][ax]
            bctmp2 = maplist[by][bx]
            if ax > 0 and ax < 9 and ay > 0 and ay < 9:
                if maplist[ay-1][ax-1] != 0 and maplist[ay-1][ax+1] != 0 and maplist[ay+1][ax-1] != 0 and maplist[ay+1][ax+1] != 0:
                    if bctmp > maplist[ay-1][ax-1]:
                        bctmp = maplist[ay-1][ax-1]

            elif bx > 0 and bx < 9 and by > 0 and by < 9:
                if maplist[by-1][bx-1] != 0 and maplist[by-1][bx+1] != 0 and maplist[by+1][bx-1] != 0 and maplist[by+1][bx+1] != 0:
                    if bctmp2 > maplist[by-1][bx-1]:
                        bctmp2 = maplist[by-1][bx-1]





            sola += maplist[ay][ax]//2
            solb += maplist[by][bx]//2
        else:
            sola += maplist[ay][ax]
            solb += maplist[by][bx]

    print(sola, solb)

    final = sola + solb
    print(final)



