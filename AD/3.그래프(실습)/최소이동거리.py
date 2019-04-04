import sys
sys.stdin = open("최소이동거리_input.txt")

'''
A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.

구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.

모든 연결 지점을 거쳐가야 하는 것은 아니다.




그림은 입력인 N=2, E=3, 시작과 끝 지점, 구간 거리가 아래와 같은 경우의 예이다.

0 1 1
0 2 6
1 2 1


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 연결지점 번호N과 도로의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례로 주어진다. ( 1<=T<=50, 1<=N, s, e<=1000, 1<=w<=10, 1<=E<=1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''


def getMinIdx():
    minV = 999999  #
    minIdx = 0
    for i in range(N + 1):  # 방문 안 한 노드 중 D가 최소인 노드 찾기
        if visit[i] == 0 and D[i] < minV:
            minIdx = i
            minV = D[i]
    return minIdx


def dijkstra(goal):
    D[0] = 0  # 출발점의 가중치

    for i in range(N + 1):
        if adj[0][i]:  # 출발점과 인접한 노드
            D[i] = adj[0][i]  # D 초기화
    visit[0] = 1  # 시작노드

    while True:
        node = getMinIdx()
        visit[node] = 1  # D가 가장 작은 노드 방문처리
        if node == goal:  # 도착지에 도착하면
            return D[goal]

        for x in range(N + 1):
            if adj[node][x]:  # minIdx에 인접인 노드에 대해
                if D[x] > (D[node] + adj[node][x]):  # minIdx를 경유하는 비용이 더 작으면
                    D[x] = D[node] + adj[node][x]  # D[x] 갱신

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visit = [0] * (N + 1)  # 방문처리
    D = [99999999] * (N + 1)  # 0번 부터의 거리(가중치)

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w  # 방향성 있음
    print('#{} {}'.format(tc, dijkstra(N)))
