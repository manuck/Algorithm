import sys
sys.stdin = open("0228_input.txt")

V = 100
D = [0] * (V+1)

def bfs(a):
    global D
    visit = [0] * (V+1)

    Q = []
    Q.append(a)

    while len(Q) > 0:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = 1
                Q.append(w)
    res = D[a]
    for i in range(V+1):
        if not visit[i]:
            continue
        if D[res] <= D[i]:
            res = i

    return res


for case in range(1, 11):
    N, start = map(int, input().split())


    G = [[0] for _ in range(V+1)]
    # print(G)
    arr = list(map(int, input().split()))

    for i in range(0, N, 2):
        G[arr[i]].append(arr[i + 1])

    # print(f"#{case} {bfs(start)}")