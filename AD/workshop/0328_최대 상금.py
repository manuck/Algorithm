import sys
sys.stdin = open("input(0328).txt")

t = int(input())

for case in range(1,t+1):
    a, n = list(map(int, input().split()))
    # print(a)
    # print(n)
    a = list(map(int, str(a)))
    # c = sorted(a)
    c = a[:]
    # print(a.index(max(a)))
    # print(a[a.index(max(a))])
    b = 0
    ind = 0
    b = a.index(max(a))
    if a[0] == a[b]:
        print('asd')
        c.pop(0)

    for i in range(n):
        # print(a)
        for j in range(len(a) - 1, ind, -1):
            if max(c) == a[j]:
                b = j
                break
        if c:
            if a[ind] < max(c):
                # b = a.index(max(a))
                a[ind], a[b] = a[b], a[ind]
                c.pop(b)
        else:
            a[-1], a[-2] = a[-2], a[-1]
        ind += 1

    # print(c)
    print(a)