import sys
sys.stdin = open("그래프 경로_input.txt")


def dfs(v):
    global G, visited, V, flag, g
    visited[v] = 1
    if v == g:
        flag = 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w]==0:
            dfs(w)


T = int(input())
for case in range(1, T+1):
    flag=0
    V, E = map(int, input().split())
    a = []
    G = [[0 for i in range(V + 1)] for j in range(V + 1)]
    visited = [0 for i in range(V + 1)]
    for i in range(E):
        data1, data2 = map(int, input().split())
        a.append(data1)
        a.append(data2)

    s, g = map(int, input().split())
    for i in range(E):
        G[a[i * 2]][a[i * 2 + 1]] = 1


    dfs(s)
    print(f'#{case} {flag}')