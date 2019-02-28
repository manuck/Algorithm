import sys
sys.stdin = open("노드의 거리_input.txt")

def bfs(v):
    global G, V, visited
    queue = []
    queue.append(v)
    visited[v] = 1

    while len(queue) != 0:
        t = queue.pop(0)

        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1

t = int(input())
for case in range(1,t+1):
    V, E = map(int, input().split())
    temp = []
    G = [[0 for _ in range(V+1)]for _ in range(V+1)]

    for i in range(E):
        data1, data2 = map(int, input().split())
        temp.append(data1)
        temp.append(data2)

    start, end = map(int, input().split())

    visited = [0] * (V+1)
    for i in range(E):
        G[temp[i*2]][temp[i*2+1]] = 1
        G[temp[i*2+1]][temp[i*2]] = 1

    bfs(start)

    if visited[end]==0:
        print(f'#{case} {visited[end]}')
    else:
        print(f'#{case} {visited[end]-visited[start]}')