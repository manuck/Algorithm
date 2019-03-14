import sys
sys.stdin = open("회문1_input.txt")

for case in range(1, 11):
    n = int(input())

    a = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        a[i] = list(input())
        # print(a[i])

    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if a[i][j:j + n] == a[i][j:j + n][::-1]:
                cnt += 1
                # print(a[i][j:j+n])

    b = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            b[i][j] = a[j][i]
    # print(a)

    for i in range(8):
        for j in range(8 - n + 1):
            if b[i][j:j + n] == b[i][j:j + n][::-1]:
                # print(b[i][j:j+n])
                cnt += 1
    res = ''
    res += '#'
    res += str(case)
    res += ' '
    res += str(cnt)
    print(res)