import sys
sys.stdin = open("subtree_input.txt")

def inorder_traverse(T): #중위
    global cnt
    if T:
        inorder_traverse(tree[T][0])
        # print(T, end=" ")
        cnt+=1
        inorder_traverse(tree[T][1])

t = int(input())
for case in range(1,t+1):
    cnt = 0
    E, N = map(int, input().split())
    V = E+1
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]
    temp = list(map(int, input().split()))

    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2

        tree[n2][2] = n1
    # print(tree)
    inorder_traverse(N)
    print('#', end="")
    print(str(case),end=" ")
    print(cnt)