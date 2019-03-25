import sys
sys.stdin = open("이진탐색_input.txt")


def inorder_traverse(T): #중위
    global V, index
    if T <= V:
        inorder_traverse(2*T)
        index.append(li[T])
        inorder_traverse(2*T+1)

t = int(input())
for case in range(1, t+1):
    V = int(input())
    E = V-1
    li = [0]
    index = []
    for i in range(1, V+1):
        li.append(i)
    a = [0]*(V+1)
    # print(li)
    # print(a)
    inorder_traverse(1)
    # print(index)
    cnt =1
    for i in index:
        li[i]= cnt
        cnt+=1
    # print(li)
    print("#", end="")
    print(str(case),end=" ")
    print(li[1], end=" ")
    print(li[V//2])

s=[]
while len(n) != 0 :
    mergeSort(n)
    n1 = n.pop(0)
    n2 = n.pop(0)
    s.append(n1 + n2)
    if len(n) == 0 :
        break
    else :
        n = [n1 + n2] + n
print(s)
print(sum(s))