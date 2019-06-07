def dfs(v):
    global G, visited, V
    s = []

    s.append(v)
    while len(s) != 0:
        v = s.pop()
        if visited[v] == 0:
            visited[v] = 1
            print(v, end=" ")
            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    s.append(w)




import sys
sys.stdin = open("연습3_input.txt")


V, E = map(int, input().split())
temp = list(map(int, input().split()))

print(temp)
G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 배열
visited = [0 for i in range(V+1)]

for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

for i in range(1, V+1):
    print("{} {}".format(i, G[i]))

print(dfs(1))