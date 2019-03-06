def inorder_traverse(T): #중위
    if T:
        inorder_traverse(tree[T][2])
        print(tree[T][1], end="")
        inorder_traverse(tree[T][3])

import sys
sys.stdin = open("0306_1_input.txt")

for case in range(1,11):
        n = int(input())
        tree = [[0 for _ in range(4)]for _ in range(n)]
        for i in range(n):
            tree[i] = list(map(str, input().split()))
            if len(tree[i]) != 4:
                while len(tree[i]) != 4:
                    tree[i].append('0')
        #     print(tree[i])
        # print(tree)
        for i in range(n):
            for j in range(4):
                if tree[i][j].isdecimal():
                    tree[i][j] = int(tree[i][j])
        tree.insert(0, [0]*4)
        # print(tree)
        print('#', end="")
        print(str(case), end=" ")
        inorder_traverse(1)
        print()