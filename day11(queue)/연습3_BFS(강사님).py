import sys
sys.stdin = open("연습3_input.txt")

def bfs(v):
    global G, V, visited
    # visited = [0] * (V+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v, end=" ")
    while len(queue) != 0:
        t = queue.pop(0)
        # v = queue.pop(0)
        # if not visited[v]:
        #     visited[v] = 1
        #     print(v, end=" ")
        for w in range(1, V+1):
            # if G[v][w] == 1 and visited[w] == 0:
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                print(w, end=" ")

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)]for _ in range(V+1)]

visited = [0] * (V+1)
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

for i in range(1, V+1):
    print("{} {}".format(i, G[i]))

# print(visited)
bfs(1)
print(visited)