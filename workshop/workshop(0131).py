import sys
sys.stdin = open("0131_input.txt")

for case in range(10):
    t = int(input())
    a = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        a[i]  = list(input())
    res = 0
    for y in range(100):
        li = []
        for x in range(100):
            li.append(a[x][y])
            for k in range(1,101):
                if a[y][x:k] == a[y][x:k][::-1] and res < len(a[y][x:k]):
                    res = len(a[y][x:k])

        for i in range(100):
            for j in range(100):
                if li[i:j] == li[i:j][::-1] and res < len(li[i:j]):
                    res = len(li[i:j])

    print(f'#{case+1} {res}')