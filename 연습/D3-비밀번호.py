import sys
sys.stdin = open("비밀번호_input.txt")

for case in range(1,11):
    n, a = list(map(int, input().split()))

    a = list(map(int, str(a)))
    # print(a)
    res =''
    while True:
        cnt = 0
        for i in range(len(a)-1):
            # print(a[i])
            if a[i] == a[i+1]:
                cnt += 1
                a.pop(i)
                a.pop(i)
                break
        if a[0] == 0:
            a.pop(0)

        if cnt == 0:
            break

    for i in a:
        res += str(i)

    print('#%i %s' %(case, res))
