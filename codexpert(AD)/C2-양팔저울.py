import sys
sys.stdin = open("C2_input.txt")

def dfs(no, lsum, rsum):
    global sol
    # if sol : return  # 가지치기
    # 현재 추를 사용(왼쪽, 오른쪽저울)하거나 사용하지 않는 경우의 수
    if no >= cn:
        # for i in range(cn): print(rec[i], end=" ")
        # print(lsum, rsum)
        if lsum == rsum:
            sol = 1
        return
    temp = abs(lsum-rsum)
    if temp > rec[no]: return
    # 현재 추를 왼쪽에 올려보기
    dfs(no + 1, lsum + chu[no], rsum)
    # 현재 추를 오른쪽에 올려보기
    dfs(no + 1, lsum, rsum + chu[no])
    # 현재 추를 사용 X
    dfs(no + 1, lsum, rsum)

cn = int(input())
chu = list(map(int, input().split()))
bn = int(input())
ball = list(map(int, input().split()))
rec = [0] * cn
# # print(ball)
for i in range(cn): # 남은 잔량
    rec[i] = sum(chu[i:cn])

for i in range(bn):
    sol = 0
    dfs(0, ball[i], 0)  # 0번추부터 시작, 왼쪽저울에 구슬값으로, 오른저울 0
    if sol:
        print('Y')
    else:
        print('N')