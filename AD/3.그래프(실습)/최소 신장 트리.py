import sys
sys.stdin = open("최소 신장 트리_input.txt")

'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
'''

def mst():
    total = 0
    u = 0       # 시작점을 0으로
    d[u] = 0
    for i in range(V+1):    # 가중치 최소값 찾기
        min = 9999999999
        for v in range(V+1):
            if visit[v] == 0 and min > d[v]:
                min = d[v]
                u = v
        visit[u] = 1        # 방문처리
        total += g[pi[u]][u]

        for v in range(V+1):    # 인접한 정점 업데이트
            if g[u][v] != 0 and visit[v] == 0 and g[u][v] < d[v]:
                d[v] = g[u][v]
                pi[v] = u

    return total


t = int(input())
for case in range(1, t+1):
    V, E = map(int, input().split())
    d = [99999999999] * (V+1)
    pi = list(range(V+1))
    g = [[0 for _ in range(V+1)]for _ in range(V+1)]
    visit = [0] * (V + 1)
    for i in range(E):
        n1, n2, w = list(map(int, input().split()))
        g[n1][n2] = g[n2][n1] = w

    a = mst()
    print('#%i %i' % (case, a))


