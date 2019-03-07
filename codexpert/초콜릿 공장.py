import sys
sys.stdin = open("초콜릿 공장_input.txt")


n = int(input())
res = 0
for case in range(n):
    L, H = map(str, input().split())
    # print(L, H)
    cnt = 0
    lcnt = 0
    hcnt = 0
    for i in L:
        for j in H:
            if i == j:
                cnt += 1

    for i in range(len(L)):
        for j in range(len(L)):
            if i != j:
                if L[i] == L[j]:
                    lcnt += 1

    for i in range(len(H)):
        for j in range(len(H)):
            if i != j:
                if H[i] == H[j]:
                    lcnt += 1

    if cnt > 2 or lcnt != 0:
        res += 1
print(res)