import sys
sys.stdin = open("0221_input.txt")


def cal(number):
    i = 0
    stack = []
    back = []
    while i < len(number):

        if number[i] == '*':
            if len(stack) != 0:
                while len(stack) != 0 and stack[0] == '*':
                    back.append(stack.pop(0))
            stack.insert(0, number[i])

        elif number[i] == '+':
            if len(stack) != 0:
                while len(stack) != 0:
                    back.append(stack.pop(0))
            stack.insert(0, number[i])

        elif number[i] == '(':
            a = cal(number[i + 1:])
            back += a[0]
            i += a[1] + 1

        elif number[i] == ')':
            back.extend(stack)
            return [back, i]

        else:
            back.append(number[i])

        i += 1
    back.extend(stack)
    return back


for case in range(1, 11):
    n = input()
    a = list(input())
    back = cal(a)
    stack = []

    for i in back:

        if i == '+':
            result = int(stack.pop(0)) + int(stack.pop(0))
            stack.insert(0, result)

        elif i == '*':
            result = int(stack.pop(0)) * int(stack.pop(0))
            stack.insert(0, result)
        else:
            stack.insert(0, i)

    print(f'#{case} {result}')