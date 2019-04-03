import sys
sys.stdin = open("최소 신장 트리_input.txt")

def mst():
    total = 0
    u = 0       # 시작점을 0으로
    d[u] = 0
    for i in range(V+1):    # 가중치 최소값 찾기
        min = 9999999999
        for v in range(V+1):
            if visit[v] == 0 and min > d[v]:
                min = d[v]
                u = v
        visit[u] = 1        # 방문처리
        total += g[pi[u]][u]

        for v in range(V+1):    # 인접한 정점 업데이트
            if g[u][v] != 0 and visit[v] == 0 and g[u][v] < d[v]:
                d[v] = g[u][v]
                pi[v] = u

    return total


t = int(input())
for case in range(1,t+1):
    V, E = map(int, input().split())
    d = [99999999999] * (V+1)
    pi = list(range(V+1))
    g = [[0 for _ in range(V+1)]for _ in range(V+1)]
    visit = [0] * (V + 1)
    for i in range(E):
        n1, n2, w = list(map(int, input().split()))
        g[n1][n2] = g[n2][n1] = w

    a = mst()
    print('#%i %i' % (case,a))


