import sys
sys.stdin = open("0307_input.txt")

def postorder_traverse(T):  # 후위순회
    if T:
        postorder_traverse(a[T][2])
        postorder_traverse(a[T][3])
        res.append(a[T][1])

for case in range(1, 11):
    n = int(input())
    a = [[0 for _ in range(3)] for _ in range(n)]
    res = []
    for i in range(n):
        a[i] = list(map(str, input().split()))

    # print(a)
    for i in range(n):
        if len(a[i]) != 4:
            while len(a[i]) != 4:
                a[i].append('0')
    # print(a)
    for i in range(n):
        for j in range(4):
            if a[i][j].isdecimal():
                a[i][j] = int(a[i][j])

    a.insert(0, [0, 0, 0, 0])
    # print(a)

    postorder_traverse(1)
    # print(res)
    cal = []
    for i in res:
        if i == '-':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num2 - num1)

        elif i == '+':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num2 + num1)

        elif i == '*':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num2 * num1)

        elif i == '/':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num2 / num1)

        else:
            cal.append(i)
    print('#', end="")
    print(str(case), end=" ")
    print(int(cal[0]))