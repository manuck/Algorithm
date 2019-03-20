import sys
sys.stdin = open("연습3_input.txt")

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

cryptos = [
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
]

def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else : return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = input()
for i in range(len(arr)):
    makeT(aToh(arr[i]))

print(t)
i = 0
while True:
    for j in range(10):
        # print(t[i:i+6])
        if t[i:i+6] == cryptos[j]:
            i = i+5
            print(j, end=" ")
    i += 1
    if i >= len(t):
        break

