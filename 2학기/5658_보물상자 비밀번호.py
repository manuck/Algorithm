import sys
sys.stdin = open("보물상자 비밀번호_input.txt")

t = int(input())

for case in range(1,t+1):
    n, k = map(int, input().split())
    a = list(input())
    # print(k)
    # hex 값 int로 출력
    # for i in range(len(a)):
    #     print(int(a[i],16))
    side = n//4
    hexlist = []
    for i in range(side):
        # print(a)
        b = a.pop()
        a.insert(0, b)
        z=0
        for q in range(4):
            hexstr = ""
            for j in range(side):
                hexstr += a[j+z]
            # print(hexstr)
            if hexstr not in hexlist:
                hexlist.append(hexstr)
            z += side
    for i in range(len(hexlist)):
        hexlist[i] = int(hexlist[i], 16)

    hexlist.sort(reverse=True)
    # print(hexlist)
    # print(k)
    print('#%i %i' % (case, hexlist[k-1]))
