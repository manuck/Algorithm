import sys
sys.stdin = open("Forth_input.txt")

t = int(input())
for case in range(1, t+1):
    a = list(map(str, input().split()))
    res = []
    sumnum = 0
    er = 0

    for i in range(len(a)):
        if a[i].isdecimal():
            res.append(a[i])

        else:
            if a[i] == '+':

                if len(res) < 2:
                    er = 1
                    break

                num1 = res.pop()
                num2 = res.pop()
                sumnum = int(num1) + int(num2)
                res.append(sumnum)

            elif a[i] == '-':

                if len(res) < 2:
                    er = 1
                    break

                num1 = res.pop()
                num2 = res.pop()
                sumnum = int(num2) - int(num1)
                res.append(sumnum)

            elif a[i] == '*':

                if len(res) < 2:
                    er = 1
                    break
                num1 = res.pop()
                num2 = res.pop()
                sumnum = int(num1) * int(num2)
                res.append(sumnum)

            elif a[i] == '/':

                if len(res) < 2:
                    er = 1
                    break

                num1 = res.pop()
                num2 = res.pop()
                sumnum = int(num2) // int(num1)
                res.append(int(sumnum))

            elif a[i] == '.':
                if len(res) == 1:
                    result = res.pop()
                else:
                    er = 1


    if er == 1:
        print(f'#{case} error')

    else:
        if len(res) == 0:
            print(f'#{case} {result}')
        else:
            print(f'#{case} error')

