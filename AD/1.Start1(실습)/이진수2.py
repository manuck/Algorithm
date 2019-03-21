import sys
sys.stdin = open("이진수2_input.txt")

t = int(input())

for case in range(1,t+1):
    a = float(input())

    n = 1
    res = ''
    b = a // (2 ** (-n))
    # print(b)
    while True:
        b = int(a//(2**(-n)))
        res += str(b)
        a = a%(2**(-n))
        n+=1
        if a == 0:
            break
        elif n > 12:
            res = 'overflow'
            break
    print('#%i' % (case), end=" ")
    print(res)