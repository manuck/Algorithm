def itoa(x):
    li = []
    while x != 0:
        a = x % 10
        x = x // 10
        li.append(chr(a + ord('0')))

    li = li[::-1]
    li = ''.join(li)
    return li

x = 123
print(itoa(x))