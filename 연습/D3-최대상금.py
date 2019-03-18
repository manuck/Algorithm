import sys
sys.stdin = open("최대상금_input.txt")

t = int(input())

for case in range(1,t+1):
    a, n = list(map(str, input().split()))
    print(a ,n)

    # print(a)
    res =[]
    sol=''
    for i in range(len(a)):
        res.append(int(a[i]))

    # print(res)
    cnt = 0
    for i in range(len(res)):
        cnt += 1
        for j in range(len(res)):
            if res[i] < res[~j]:
                res[i], res[j] = res[j], res[i]
                break
        if cnt==n:
            break
    print(res)
    # print('#%i %s' %(case, sol))