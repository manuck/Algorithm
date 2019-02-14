import sys
sys.stdin = open("괄호검사_input.txt")


def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            s.append(data[i])
        elif data[i] == "{":
            s.append(data[i])

        elif data[i] == ")":
            if isEmpty():
                return 0
            else:
                if s[-1]=="{":
                    return 0
                else:
                    s.pop()

        elif data[i] == "}":
            if isEmpty():
                return 0
            else:
                if s[-1]=="(":
                    return 0
                else:
                    s.pop()

    if not isEmpty():
        return 0
    else:
        return 1


T = int(input())
for case in range(1,T+1):
    s = []
    a = input()
    print(f'#{case} {check_matching(a)}')