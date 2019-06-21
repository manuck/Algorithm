import sys
sys.stdin = open("무선 충전_input.txt")



t = int(input())

for case in range(1):
    maplist = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        print(maplist[i])

    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(m, n)
    print(a)
    print(b)
    for i in range(n):
        apx, apy, c, power = map(int, input().split())
        print(apx, apy, c, power)
        tmp = 0
        for j in range(apy-1, apy-c-2, -1):
            if j<0:
                pass
            print(j)
            print(tmp)
            for q in range(apx-c+tmp-1, apx+c-tmp):
                print(q, j)
                if q>=0 and q<10:
                    if maplist[j][q] < power:
                        maplist[j][q] = power
            tmp += 1
        tmp2 = 1

        for j in range(apy, apy+c):
            if j>=10:
                pass
            print(j)
            for q in range(apx-c+tmp2-1, apx+c-tmp2):

                print(q, j)
                if q >= 0 and q < 10:
                    if maplist[j][q] < power:
                        maplist[j][q] = power
            tmp2 += 1

    for i in range(10):
        print(maplist[i])





