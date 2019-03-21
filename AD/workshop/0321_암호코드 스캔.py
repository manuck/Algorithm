import sys
sys.stdin = open("input(0321_2).txt")

amho = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2],
]

asc = [[0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]]

def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else : return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        z.append(asc[x][i])


t = int(input())    # t = 테스트 케이스

for case in range(1, t+1):
    n, m = map(int, input().split())    # n = 세로, m = 가로
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(input())
        # print(a[i])
    b = []
    for i in range(1, n):
        for j in range(m):
            if a[i][j] != '0' and a[i-1][j] == '0':
                # print(a[i])
                b.append(a[i])
                break
    # print(b)
    z = []
    for j in range(len(b)):
        for i in range(len(b[j])):
            makeT(aToh(b[j][i]))

    # print(z)
    temp = []
    cnt = 0
    zindex = 0
    for i in range(len(z)):
        if z[i] == 1:
            zindex=i
            break

    for i in range(len(z)-1):
        if z[i] != z[i+1]:
            cnt += 1
        if cnt == 32:
            temp.append(z[zindex:i+1])
            cnt = 0
            for j in range(i+1, len(z)):
                if z[j] == 1:
                    zindex = j

    print(temp)
    multiple = []
    for i in range(len(temp)):
        multiple.append(len(temp[i])//56 + 1)
        if len(temp[i])%56 != 0:
            while int(len(temp[i]) % 56) != 0:
                temp[i].insert(0, 0)

    #     print((temp[i]))
    # print(multiple)
    for i in range(len(temp)):
        temp[i].append(0)
    temp2 = []
    for i in range(len(temp)):
        count = 1
        temp3 = []
        for j in range(len(temp[i])-1):
            if temp[i][j] == temp[i][j+1]:
                count += 1
            elif temp[i][j] != temp[i][j+1]:
                temp3.append(count)
                count = 1
        temp2.append(temp3)



    print(temp2)
    # print(min(temp2))
    for i in range(len(temp2)):
        for j in range(len(temp2[i])):
            temp2[i][j] = int(temp2[i][j]/min(temp2[i]))

    sol = []
    for i in range(len(temp2)):
        q = 0
        res = []
        while True:
            for j in range(10):
                # print(t[~i:~(i+6])
                if temp2[i][q:q + 4] == amho[j]:
                    q = q + 3
                    res.append(j)
            q += 1
            if q >= len(temp2[i]):
                break
        sol.append(res)
    print(sol)
    for i in range(len(sol)):
        if len(sol[i])==0:
            sol.pop(i)

    nsm = []
    print('#%i' % (case), end=" ")
    for j in range(len(sol)):
        check = sol[j].pop()
        fron = []
        back = []
        # print(res)
        for i in range(len(sol[j])):
            if i % 2 == 0:
                fron.append(sol[j][i])
            else:
                back.append(sol[j][i])

        if (sum(fron) * 3 + sum(back) + check) % 10 == 0:
            nsm.append(sum(sol[j]) + check)
        else:
            nsm.append(0)

    print(sum(nsm))




