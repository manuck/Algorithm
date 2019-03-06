import sys
sys.stdin = open("연습문제_input.txt")

def preorder_traverse(T): #전위
    if T:
        print(T, end=" ")
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

def inorder_traverse(T): #중위
    if T:
        inorder_traverse(tree[T][0])
        print(T, end=" ")
        inorder_traverse(tree[T][1])

def postorder_traverse(T): # 후위순회
    if T:
        postorder_traverse(tree[T][0])
        postorder_traverse(tree[T][1])
        print(T, end=" ")

def printTree():
    for i in range(1,V+1):
        print("%2d %2d %2d %2d" %(i, tree[i][0], tree[i][1], tree[i][2]))

# V, E = map(int, input().split())
V = int(input())
tree = [[0 for _ in range(3)]for _ in range(V+1)]
temp = list(map(int, input().split()))
E = int(len(temp)/2)
print(temp)

for i in range(E):
    n1 = temp[i*2]
    n2 = temp[i*2+1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2

    tree[n2][2] = n1

print(tree)
printTree()
print()
print("전위순회 : ", end = " ")
preorder_traverse(1)
print()
print("중위순회 : ", end = " ")
inorder_traverse(1)
print()
print("후위순회 : ", end = " ")
postorder_traverse(1)









