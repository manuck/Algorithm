import sys
sys.stdin = open("연습3_input.txt")
def BFS(G, v):
    global visited
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v, end=" ")
    while queue:
        t = queue.pop(0)
        for i in range(1, E):
            if not visited[i] and G[i][t]==1:
                queue.append(i)
                visited[i] = 1
                print(i, end=" ")


V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)]for _ in range(V+1)]
visited = [0] * (V+1)

for i in range(E):
    # G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

for i in range(1, V+1):
    print("{} {}".format(i, G[i]))

# print(visited)
BFS(G, 1)