import sys
sys.stdin = open("0221_input.txt")


for case in range(1):
    n = int(input())
    a = list(input())
    res = []
    oper = []
    print(a)

    for i in range(len(a)):
        res.append(a[i])
        if not a[i].isdecimal():
            op = res.pop()
            print(op)
            if len(oper)==0:
                oper.append(op)

            if a[i] > oper[-1]:
                oper.append(op)
            else:
                z = res.pop()
                res.append(z)

    print(oper)

    # for i in range(len(oper)):
    #     op = oper.pop()
    #     res.append(op)

    print(res)