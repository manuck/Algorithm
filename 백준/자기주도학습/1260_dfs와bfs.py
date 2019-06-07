import sys
sys.stdin = open("1260.txt")

def dfs(x):
    global N, V, M
    visited[x] = 1
    print(x, end=" ")
    for w in range(1, N+1):
        if li[x][w] == 1 and visited[w] == 0:
            dfs(w)

def bfs(x):
    global N, V, M
    s = []
    s.append(x)
    visited[x] = 1
    while len(s) != 0:
        # print(s)
        # print(visited)
        k = s.pop(0)
        print(k, end=" ")
        for w in range(1, N+1):
            if li[k][w] and visited[w] == 0:
                visited[w] = 1
                s.append(w)


N, M, V = list(map(int, input().split()))

li = [[0 for _ in range(N+1)]for _ in range(N+1)]
visited = [0 for i in range(N+1)]

temp = []
for i in range(M):
    a, b = list(map(int, input().split()))
    temp.append(b)
    temp.append(a)

# print(temp)
for i in range(M):
    li[temp[i*2]][temp[i*2+1]] = 1
    li[temp[i*2+1]][temp[i*2]] = 1

# for i in range(N+1):
#     print(li[i])

dfs(V)
visited = [0 for i in range(N+1)]
print()
bfs(V)
