import sys
sys.stdin = open("input(0321).txt")

t = int(input())

for case in range(1,t+1):
    a = list(input())
    b = list(input())

    binnum = len(a)-1
    trinum = len(b)-1
    # print(a, b)
    aa = 0
    bb = 0
    for i in range(len(a)):
        if a[i] == '1':
            aa += (2**binnum)
        binnum -= 1

    for i in range(len(b)):
        if b[i] != '0':
            bb += (3**trinum)*int(b[i])
        trinum -= 1

    ali = []
    bli = []
    # print(aa, bb)
    print('#%i' % (case), end=" ")
    for i in range(len(a)):
        coa = a[:]
        if coa[i] == '0':
            coa[i] = '1'
            ali.append(coa)

    for i in range(len(b)):
        coa = b[:]
        if coa[i] == '1':
            coa[i] = '0'
            bli.append(coa)
        elif coa[i] == '2':
            coa[i] = '1'
            bli.append(coa)
    for i in range(len(b)):
        coa = b[:]
        if coa[i] == '2':
            coa[i] = '0'
            bli.append(coa)

    for i in range(len(a)):
        coa = a[:]
        if coa[i] == '1':
            coa[i] = '0'
            ali.append(coa)

    for i in range(len(b)):
        coa = b[:]
        if coa[i] == '1':
            coa[i] = '2'
            bli.append(coa)

    for i in range(len(b)):
        coa = b[:]
        if coa[i] == '0':
            coa[i] = '1'
            bli.append(coa)

    for i in range(len(b)):
        coa = b[:]
        if coa[i] == '0':
            coa[i] = '2'
            bli.append(coa)
        #
    for i in range(len(ali)):
        binnum = len(ali[i]) - 1
        aa = 0
        for j in range(len(ali[i])):
            if ali[i][j] == '1':
                aa += (2 ** binnum)
            binnum -= 1
        ali[i] = aa

    for i in range(len(bli)):
        trinum = len(bli[i]) - 1
        bb = 0
        for j in range(len(bli[i])):
            if bli[i][j] != '0':
                bb += (3 ** trinum) * int(bli[i][j])
            trinum -= 1
        bli[i] = bb
    # print(ali)
    # print(bli)

    res = 0
    for i in ali:
        for j in bli:
            if i == j:
                print(i)

''' 강사님 코드
def toDec(x, mode):
    value = 0
    for i in range(len(x)):
        value = value * mode + int(x[i])
    return value

TC = int(input())
for tc in range(1, TC + 1):
    str2 = input()
    str3 = input()

    list2 = []
    list3 = []

    #2진수
    for i in range(len(str2)):
        x2 = list(str2)
        x2[i] = str((int(x2[i]) + 1) % 2)
        list2.append(toDec(x2, 2))
        #list2.append(int("".join(x2), 2))
    #3진수
    for i in range(len(str3)):
        for j in [1, 2]:
            x3 = list(str3)
            x3[i] = str((int(x3[i]) + j) % 3)
            list3.append(toDec(x3, 3))

    # 같은값 찾기
    for i in range(len(list2)):
        for j in range(len(list3)):
            if list2[i] == list3[j]:
                ans = list2[i]
                break

    print("#%d" % tc, ans)
'''
