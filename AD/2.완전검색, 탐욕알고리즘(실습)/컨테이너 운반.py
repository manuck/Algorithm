import sys
sys.stdin = open("컨테이너 운반_input.txt")

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    cont = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    index = 0
    cont.sort(reverse=True)
    truck.sort(reverse=True)
    res = 0

    flag = 1
    while flag:
        if truck[0] >= cont[0]:
            res += cont.pop(0)
            truck.pop(0)
        else:
            cont.pop(0)

        if not cont:
            flag = 0
        if not truck:
            flag = 0


    print('#%i '% (case), end="")
    print(res)

