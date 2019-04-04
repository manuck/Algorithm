import sys
sys.stdin = open("연산_input.txt")

'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
'''

def BFS(v):
    global visited, q, D
    f = 0
    q.append(v)
    visited[v] = 1
    while D[M] == 0:
        n = q[f]
        f += 1
        for i in range(4):
            if arr[i] != 2:
                temp = n + arr[i]
            else:
                temp = n * 2
            if temp > 0 and temp <= 2 * M:
                if visited[temp] == 0:
                    visited[temp] = 1
                    D[temp] = D[n] + 1
                    q.append(temp)
                else:
                    if D[temp] > 1 + D[n]:
                        D[temp] = 1 + D[n]
                        q.append(temp)


t = int(input())
for case in range(1, t + 1):
    N, M = map(int, input().split())
    q = []
    visited = [0 for _ in range(2 * M)]
    D = [0 for _ in range(2 * M)]
    arr = [1, -1, -10, 2]
    BFS(N)
    print('#%i %i' % (case, D[M]))