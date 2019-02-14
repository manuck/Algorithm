import sys
sys.stdin = open("0214_input.txt")

# def dfs(v):
#     global G, visited, V, flag, g
#     visited[v] = 1
#
#     if v == g:
#         flag = 1
#     for w in range(1, V+1):
#         if G[v][w] == 1 and visited[w]==0:
#             dfs(w)
#

# def indegree(gra, *g):



for case in range(1, 5):

    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    res = []
    G = [[0 for i in range(V + 1)]for j in range(V + 1)]  # 2차원 배열
    visited = [0 for i in range(V + 1)]

    for i in range(E):
        # G[temp[i * 2]][temp[i * 2 + 1]] = 1
        G[temp[i * 2 + 1]][temp[i * 2]] = 1


    for i in range(1, V + 1):
        print("{} {}".format(i, G[i]))



