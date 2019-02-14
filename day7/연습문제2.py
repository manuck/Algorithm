def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)

def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False

s = []
def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        elif data[i] == ")":
            pop()
    if not isEmpty():
        return False
    else:
        return True

print(check_matching('()()((()))'))














    # le = ['[','{','(']
    # ri = [']', '}', ')']
    # lec = 0
    # ric = 0
    # for i in a:
    #     if i in le:
    #         lec += 1
    #     elif i in ri:
    #         ric += 1
    # if lec == ric:
    #     return True
    # else:
    #     return False