import sys
sys.stdin = open("이진수_input.txt")

asc = [[0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]]

def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else : return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        z.append(asc[x][i])

t = int(input())

for case in range(1,t+1):
    n, a = list(map(str, input().split()))

    z = []
    for i in range(len(a)):
        makeT(aToh(a[i]))

    print('#%i' % (case), end=" ")
    for i in range(len(z)):
        print(z[i], end="")
    print()



