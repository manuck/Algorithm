import sys
sys.stdin = open("D1_input.txt")

def check(no, color):
    # 현 노드와 연결된 인접한 노드와 중복 색상 여부 체크
    for i in range(no):
        if arr[no][i] and visit[i] == color: return 0
    return 1

def dfs(no):
    global sol
    # 현재 노드에서 1~M번색까지 모두 칠해보는 경우의 수
    if no >= n:
        sol = 1
        return
    # 현노드에게 현 색상을 칠할 수 있으면 칠하고 다음 노드로 진행
    for i in range(1, m+1):
        if check(no, i):
            visit[no] = i
            dfs(no+1)
            if sol: return

n, m = map(int, input().split())
arr = []
visit = [0] * n
sol = 0
for i in range(n):
    arr.append(list(map(int, input().split())))

dfs(0)
print(sol)



