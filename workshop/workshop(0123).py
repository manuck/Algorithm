import sys
sys.stdin = open("0123_input.txt")

def mymax(li):
    maxN = 0
    for i in range(len(li)):
        if maxN < li[i]:
            maxN = li[i]
    return maxN

for i in range(10):
    n = input()
    a = [[0 for _ in range(100)] for _ in range(100)]
    for j in range(100):
        a[j] = list(map(int, input().split()))
    b = []
    for j in range(len(a)):
        c = 0
        for k in range(len(a[j])):
            c += a[j][k]
        b.append(c)
    for k in range(len(a[0])):
        d = 0
        for j in range(len(a)):
            d += a[j][k]
        b.append(d)
    e = 0
    for j in range(100):
        e += a[j][j]
    b.append(e)
    f = 0
    for j in range(100):
        f += a[j][99-j]
    b.append(f)

    print(f'#{i + 1} {mymax(b)}')