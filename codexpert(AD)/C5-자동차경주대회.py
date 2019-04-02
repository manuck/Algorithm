import sys
sys.stdin = open("C5_input.txt")

def dfs(no, dsum, tsum):
    global sol
    if dsum + dist[no] > limit: return
    if no >= n:
        if tsum < sol:
            sol = tsum
            return
    dfs(no+1, dsum + dist[no], tsum)    # 정비를 받지 않기
    dfs(no+1, 0, tsum + time[no])       # 정비를 받기

def dfs2(start, tsum):
    global sol
    if tsum > sol:
        return
    if start > n:
        if tsum < sol:
            sol = tsum
        return
    tot = 0
    # 출발점에서 제한된 거리 이내에서 모두 정비를 받아보는 경우의 수 시도
    for i in range(start, n+1):
        if tot + dist[i] > limit: # 거리벗어나면 탈출
            break
        tot += dist[i]
        dfs2(i+1, tsum + time[i])

limit = int(input())
n = int(input())
dist = list(map(int, input().split()))
time = list(map(int, input().split()))
# time.append(0)
sol = 9999999
# dfs2(0, 0)
dfs(0, 0, 0)
print(sol)