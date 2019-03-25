# def solve(x):
#     t = x % 10
#     x //= 10
#     while x:
#         if x % 10 > t:
#             return False
#         t = x % 10
#         x //= 10
#     return  True

# T = int(input())
# for case in range(1, T+1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     res = -1
#     for i in range(N-1):
#         for j in range(i+1, N):
#             num = data[i] * data[j]
#             if solve(num):
#                 if res < num :
#                     res = num
#     print('#{} {}'.format(case, res))


t = int(input())

for case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    # print(a)
    num = []
    for i in range(n):
        for j in range(i+1, n):
            num.append(str(a[i]*a[j]))

    # print(num)
    res = []
    for i in range(len(num)):
        if len(num[i]) == 1:
            res.append(num[i])
        for j in range(len(num[i])-1):
            if num[i][j] > num[i][j+1]:
                break
            else:
                res.append(num[i])
    #
    # print(res)
    for i in range(len(res)):
        if res[i].isdecimal():
            res[i] = int(res[i])

    # print(res)
    print('#%i' % (case), end=" ")
    if len(res) == 0:
        print(-1)
    else:
        print(max(res))