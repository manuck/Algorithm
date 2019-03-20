import sys
sys.stdin = open("0320_input.txt")

amho = [
    # ['0', '0', '0', '1', '1', '0', '1'],
    # ['0', '0', '1', '1', '0', '0', '1'],
    # ['0', '0', '1', '0', '0', '1', '1'],
    # ['0', '1', '1', '1', '1', '0', '1'],
    # ['0', '1', '0', '0', '0', '1', '1'],
    # ['0', '1', '1', '0', '0', '0', '1'],
    # ['0', '1', '0', '1', '1', '1', '1'],
    # ['0', '1', '1', '1', '0', '1', '1'],
    # ['0', '1', '1', '0', '1', '1', '1'],
    # ['0', '0', '0', '1', '0', '1', '1'],
    #
    ['1', '0', '1', '1', '0', '0', '0'],
    ['1', '0', '0', '1', '1', '0', '0'],
    ['1', '1', '0', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1', '1', '0'],
    ['1', '1', '0', '0', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '1', '0'],
    ['1', '1', '1', '1', '0', '1', '0'],
    ['1', '1', '0', '1', '1', '1', '0'],
    ['1', '1', '1', '0', '1', '1', '0'],
    ['1', '1', '0', '1', '0', '0', '0'],
]

t = int(input())

for case in range(1,t+1):
    n, m = map(int, input().split())

    a = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(n):
        a[i] = list(input())
        # print(a[i])
    x = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '1':
                x = i
    b =[]
    b = a[x][::-1]
    # print(b)
    i = 0
    res = []
    while True:
        for j in range(10):
            # print(t[~i:~(i+6])
            if b[i:i+7] == amho[j]:
                i = i + 6
                res.append(j)
        i += 1
        if i >= m:
            break
    # print(res)
    res = res[::-1]
    check = res.pop()
    fron = []
    back = []
    # print(res)
    print('#%i' % (case), end=" ")
    for i in range(len(res)):
        if i%2 == 0:
            fron.append(res[i])
        else:
            back.append(res[i])

    if (sum(fron)*3+sum(back)+check)%10 == 0:
        print(sum(res)+check)
    else:
        print('0')