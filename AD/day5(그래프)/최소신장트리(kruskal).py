import sys
sys.stdin = open("최소신장트리_input.txt")

def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst_kruskal():
    global V
    cnt = 0
    total = 0
    i = 0
    while cnt < V:
        p1 = findSet(edge[i][0])
        p2 = findSet(edge[i][1])
        if p1 != p2:
            total += edge[i][2]
            cnt += 1
            p[p2] = p1
        i += 1
    return total


t = int(input())
for case in range(1, t+1):
    V, E = map(int, input().split())
    p = list(range(V+1))
    edge = [[0 for _ in range(3)]for _ in range(E)]
    visit = [0] * (V + 1)
    for i in range(E):
        edge[i] = list(map(int, input().split()))
        # edge[n1][n2] = edge[n2][n1] = w

    edge.sort(key=lambda k: k[2])
    a = mst_kruskal()
    print('#%i %i' % (case, a))
