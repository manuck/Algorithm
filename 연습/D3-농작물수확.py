import sys
sys.stdin = open("농작물수확_input.txt")


t = int(input())

for case in range(1, t + 1):
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i] = list(input())

    res = 0
    start = n // 2
    end = n // 2
    for i in range(n):
        for j in range(n):
            if a[i][j].isdecimal():
                a[i][j] = int(a[i][j])

    for i in range(n // 2):
        res += sum(a[i][start:~end + 1])
        end -= 1
        start -= 1

    start = 0
    end = n
    for i in range((n // 2), n):
        # print(a[i][start:end])
        res += sum(a[i][start:end])
        start += 1
        end -= 1

    print('#%i %i' % (case, res))
