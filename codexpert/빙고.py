import sys
sys.stdin = open("빙고_input.txt")

a = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    a[i] = list(map(str, input().split()))
result = 0
start = []
end = []
for i in range(5):
    qwe = list(map(int,input().split()))
    start.append(qwe)
for i in range(5):
    for j in range(5):
        end.append(start[i][j])
# print(end)

for q in range(25):
    cnt = 0

    mc = end[q]

    result += 1


    for i in range(5):
        for j in range(5):
            if int(a[i][j]) == mc:
                a[i][j] = 0
                break
    # print(a)

    for i in range(5):
        garo = 0
        for j in range(5):
            garo += int(a[i][j])
            garo += 10
        if garo == 50:
            cnt += 1

    for i in range(5):
        sero = 0
        for j in range(5):
            sero += int(a[j][i])
            sero += 10
        if sero == 50:
            cnt += 1

    ero = 0
    for i in range(5):
        ero += int(a[i][i])
        ero += 10
        if ero == 50:
            cnt += 1
    ro = 0
    for i in range(5):
        ro += int(a[i][4-i])
        ro += 10
        if ro == 50:
            cnt += 1

    if cnt >= 3:
        break


    # print(cnt)
    # print(result)
print(result)