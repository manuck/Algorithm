import sys
sys.stdin = open("0214_input.txt")

def dfs(v):
    global G, visited, V, res, noh
    if visited[v] == 1:
        return
    res.append(v)
    visited[v] = 1
    for w in range(1, V+1):
        # print(v)
        # print(visited)
        if G[w][v] == 1:
            noh[w] -= 1
            if noh[w] == 0:
                dfs(w)


for case in range(10):
    res = []
    noh =[0]
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0 for i in range(V + 1)] for j in range(V + 1)]  # 2차원 배열
    visited = [0 for i in range(V + 1)]
    for i in range(E):
        # G[temp[i * 2]][temp[i * 2 + 1]] = 1
        G[temp[i * 2 + 1]][temp[i * 2]] = 1

    # for i in range(1, V + 1):
    #     print("{} {}".format(i, G[i]))

    for i in range(1, V + 1):
        noh.append(sum(G[i]))
    # print(noh)
    for i in range(1, V + 1):
        if sum(G[i]) == 0:
            dfs(i)

    result = ' '.join(map(str, res))
    print(f'#{case+1} {result}')


