import sys
sys.stdin = open("반나누기_input.txt")

t = int(input())

for case in range(1,t+1):
    n, kmin, kmax = map(int, input().split())
    people = list(map(int, input().split()))

    # print(n, kmin, kmax)
    # print(people)

    t1 = min(people)
    t2 = max(people)
    # print(t1, t2)

    flag = 0
    maxcnt = 0
    mincnt = 0
    sol = 99

    # 반배정 불가능 할 때(최고득점자 수 제외 반배정이 안됨)
    for i in range(n):
        if people[i] == max(people):
            maxcnt += 1
    if (n - maxcnt) < 2*kmin:
        flag = 1

    # 반배정 불가능 할 때(최저득점자 수 제외 반배정이 안됨)
    for i in range(n):
        if people[i] == min(people):
            mincnt += 1
    if (n - mincnt) < 2*kmin:
        flag = 1

    while True:
        for q in range(t1, t2):
            classcom = []
            acnt = 0
            bcnt = 0
            ccnt = 0
            for i in range(n):
                if people[i] >= t2:
                    acnt += 1
                elif people[i] < t2 and people[i] >= t1:
                    bcnt += 1
                else:
                    ccnt += 1

            classcom.append(acnt)
            classcom.append(bcnt)
            classcom.append(ccnt)

            if sol > (max(classcom)-min(classcom)):
                sol = (max(classcom)-min(classcom))

            t1 += 1
        t2 -= 1
        t1 = min(people)
        if t1 == t2:
            break

    if flag == 1:
        print(-1)
    else:
        print(sol)