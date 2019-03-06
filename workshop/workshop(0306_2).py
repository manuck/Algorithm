import sys
sys.stdin = open("0306_2_input.txt")

def inorder_traverse(T): #중위
    global cnt
    if T:
        inorder_traverse(tree[T][0])
        # print(T, end=" ")
        cnt += 1
        inorder_traverse(tree[T][1])

def check1(a):
    global li
    if tree[a][2]!=0:
        li.append(tree[a][2])
        b = tree[a][2]
        check1(b)

def rescheck(a):
    global res
    if tree[a][2] != 0:
        if tree[a][2] in li:
            res = tree[a][2]
            return res
        else:
            rescheck(tree[a][2])

t = int(input())
for case in range(1,11):
    V, E, data1, data2 = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    cnt = 0
    li = []
    res = 0
    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2

        tree[n2][2] = n1
    # for i in range(E):
    #     print(tree[i])

    if data1 < data2:
        check1(data2)
        rescheck(data1)
    elif data1 > data2:
        check1(data1)
        rescheck(data2)
    # print(li)
    print('#', end="")
    print(str(case), end=" ")
    print(res, end=" ")
    inorder_traverse(res)
    print(cnt, end=" ")
    print()