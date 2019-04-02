import sys
sys.stdin = open("D0_input.txt")

def ff(no):
    global sol
    # 현재 컴퓨터에서 연결되어 있고 감염안된 컴퓨터를 감염시키면서 카운트
    for i in range(1, n+1):
        if arr[no][i] and visit[i] == 0:
            visit[i] = 1
            sol += 1
            ff(i)

n = int(input())
m = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
visit = [0] * (n+1)
for i in range(m):
    # for j in range(n):
    #     print(arr[j])
    # print()
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

sol = 0
visit[1] = 1
ff(1)
print(sol)