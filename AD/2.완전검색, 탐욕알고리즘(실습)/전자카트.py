import sys
sys.stdin = open("전자카트_input.txt")

'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89


e   1   2   3   도착
1   0   18  34
2   48  0   55
3   18  7   0
출발

이 경우 최소 소비량은 89가 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
'''

def perm(n, k):
    sol = 0
    fir = 0
    if n == k:
        # print(a)
        b = a[:]
        b.append(1)
        # print(b)
        for i in b:
            # print(arr[fir][i-1])
            sol += arr[fir][i-1]
            fir = i-1
        res.append(sol)

    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
        # print(arr[i])
    a = list(range(2, n+1))
    # print(a)
    res = []
    perm(n-1, 0)
    ans = min(res)
    print('#%i %i' % (case, ans))
