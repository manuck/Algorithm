import sys
sys.stdin = open("화물 도크_input.txt")

t = int(input())

for case in range(1, t+1):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    # print(a)
    a.sort(key=lambda a:a[1])
    # print(a)
    cnt = 1
    i = 0
    flag = 0
    while True:
        if i >= n-1 or flag == 1:
            break
        for j in range(i+1, n):
            if a[i][1] <= a[j][0]:
                # print(a[j])
                cnt += 1
                i = j
                break
            if j == n-1:
                flag = 1
    print('#%i' % (case),end=" ")
    print(cnt)