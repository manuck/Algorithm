import sys
sys.stdin = open("이진탐색_input.txt")



t = int(input())
for case in range(1):
    V = int(input())
    tree = [[0 for _ in range(3)]for _ in range(V+1)]
    print(tree)
    num = V
    # for i in range(V,1,-1):
    #     p = i//2
    #     tree[i][2]= p
    k = 0
    while V-k != 0:
        p = num//2
        tree[num][2] = p
        num = p
        k+=1
    print(tree)