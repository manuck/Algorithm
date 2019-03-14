import sys
sys.stdin = open("메모리복구_input.txt")

t = int(input())

for case in range(1,t+1):
    a = list(input())

    init = ['0']*len(a)
    # print(a)
    # print(init)
    cnt = 0
    for i in range(len(a)):
        if a[i] != init[i]:
            # print(init)
            cnt += 1
            if init[i] == '1':
                for j in range(i, len(a)):
                    init[j] = '0'
            elif init[i] == '0':
                for j in range(i, len(a)):
                    init[j] = '1'

        if a == init:
            break

    print('#%i %i' %(case, cnt))

