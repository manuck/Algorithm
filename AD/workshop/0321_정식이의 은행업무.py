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
