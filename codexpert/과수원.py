import sys
sys.stdin = open("과수원_input.txt")

n = int(input())
a = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input()))


res = 0
for i in range(1, n):
    for j in range(1, n):
        flag = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        cnt=0
        for k in range(i):
            for q in range(j):
                if a[k][q] == 1:
                    cnt1 += 1

        for k in range(i):
            for q in range(j, n):
                if a[k][q] == 1:
                    cnt2 += 1

        for k in range(i, n):
            for q in range(j):
                if a[k][q] == 1:
                    cnt3 += 1

        for k in range(i, n):
            for q in range(j, n):
                if a[k][q] == 1:
                    cnt4 += 1

        if cnt1 == cnt2 and cnt2 == cnt3 and cnt3 == cnt4:
            flag = 1
            res += 1

    #
    # if flag == 1:
    #     print(res)
    #     break
    # else:
    #     print(-1)

if res > 0 :
    print(res)
else:
    print(-1)