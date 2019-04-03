import sys
sys.stdin = open("최소합_input.txt")

'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
 
1 2 3
2 3 4 
3 4 5

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

dx = [0, 1]
dy = [1, 0]

def dfs(x, y, res):
    global n, flag, sol
    if sol:
        if min(sol) <= res:
            return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if ny == n or nx == n: continue
        if ny == n-1 and nx == n-1:
            flag = 1
            if sol:
                if min(sol) > res:
                    sol.append(res)
            else:
                sol.append(res)
            res = 0
            break
        dfs(nx, ny, res + arr[ny][nx])

    if flag == 1:
        return res

t = int(input())
for case in range(1,t+1):
    n = int(input())
    arr = [[0 for _ in range(n)]for _ in range(n)]
    visited = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    flag = 0
    sx, sy = 0, 0
    res = 0
    resmin = 888888
    sol = []
    dfs(sx, sy, res)

    print('#%i '%(case), end="")
    print(sol[-1]+arr[0][0]+arr[n-1][n-1])






