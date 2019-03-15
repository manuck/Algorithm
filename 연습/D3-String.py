import sys
sys.stdin = open("String_input.txt", 'rt', encoding='UTF8')


for case in range(1,11):
    n = int(input())
    a = list(input())
    b = list(input())
    cn = len(a)
    res = 0
    for i in range(len(b)-cn+1):
        if b[i:i+cn] == a:
            res += 1

    print('#%i %i' % (case,res))