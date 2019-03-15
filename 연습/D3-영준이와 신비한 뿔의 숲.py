import sys
sys.stdin = open("영준이와 신비한 뿔의 숲_input.txt")

t = int(input())

for case in range(1, t+1):
    n, m = list(map(int, input().split()))
    uni = 0
    twin = 0
    i = 0
    while True:
        twin = (n-i)//2
        uni = ((n-i)%2)+i

        if twin + uni == m:
            break
        else:
            i += 1

    print('#%i %i %i'  % (case, uni, twin))
