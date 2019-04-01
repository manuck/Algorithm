import sys
sys.stdin = open("C3_input.txt")


def dfs(no, lastA, lastB, hap):
    global sol
    if no >= n:
        if hap > sol:
            sol = hap
        return
    # A : 작은 상자순으로 포장하기
    if lastA > box[no]:
        dfs(no+1, box[no], lastB, hap+box[no])

    # B : 큰 상자순으로 포장하기
    if lastB < box[no]:
        dfs(no+1, lastA, box[no], hap+box[no])
    dfs(no+1, lastA, lastB, hap)




t = int(input())
for case in range(1,t+1):
    n = int(input())
    box = list(map(int, input().split()))
    # print(box)
    sol = 0
    dfs(0, 1000, 0, 0)

    print(sol)
