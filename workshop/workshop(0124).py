import sys
sys.stdin = open("0124_input.txt")

t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    fo = []
    ba = []
    result = []
    for i in range(len(a)):
        if i % 2 == 0:
            fo.append(a[i])
        else:
            ba.append(a[i])

    for i in range(len(fo)):
        if fo[i] not in ba:
            fo_index = i
            result.append(fo[i])
            result.append(ba[i])
    i = 0
    while len(result) < 2 * n:
        for i in range(len(fo)):
            if result[~0] == fo[i]:
                index = i
                result.append(fo[i])
                result.append(ba[i])

    result = ' '.join(map(str,result))
    print(f'#{k+1} {result}')