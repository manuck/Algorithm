import sys
sys.stdin = open("이진 힙_input.txt")

def enQ(n):
    global last
    last += 1           # 마지막 노드번호 증가
    c = last            # 마지막 노드를 자식 노드로
    p = c//2            # 부모 노드 번호 계산
    Q[last] = n         # 마지막 노드에 값 저장
    while c > 1 and Q[p] > Q[c]:        # 루트가 아니고, 부모 노드의 값이 더 크면
        Q[p], Q[c] = Q[c], Q[p]         # 저장된 값 바꿈
        c = p                           # 부모를 새로운 자식 노드로
        p = p//2


t = int(input())
for case in range(1,t+1):
    V = int(input())
    a = list(map(int, input().split()))
    Q = [0]*(V+1)
    last = 0
    for i in range(V):
        enQ(a[i])

    # print(a)
    # print(Q)
    index = V//2
    res = 0
    while index != 0:
        res += Q[index]
        index //= 2

    print('#', end="")
    print(str(case), end=" ")
    print(res)

