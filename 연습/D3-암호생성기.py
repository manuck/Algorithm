import sys
sys.stdin = open("암호생성기_input.txt")

for case in range(1, 11):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 1
    while True:
        b = a.pop(0)
        b -= cnt
        if b <= 0:
            b = 0
            a.append(b)
            break
        a.append(b)

        cnt+=1
        if cnt == 6:
            cnt=1

    print('#%i' % (n), end=" ")
    for i in a:
        print(i, end=" ")
    print()
