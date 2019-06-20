import sys
sys.stdin = open("특이한 자석_input.txt")

def clockwise(a):
    z = a[:]
    tmp = z.pop()
    z.insert(tmp, 0)
    print('asd')
    return z

def anticlockwise(a):
    z = a[:]
    tmp = z.pop(0)
    z.append(tmp)
    print('dsa')
    return z

t = int(input())

for case in range(1):
    k = int(input())

    gear = []
    for i in range(4):
        gear.append(list(map(int,input().split())))

    for i in range(4):
        print(gear[i])

    for i in range(k):
        n, wise = map(int, input().split())
        print(n, wise)

        if gear[n-2] == True:
            q = n-1
            while  q >= 0:
                if gear[q][6] != gear[q-1][2]:
                    if wise == 1:
                        gear[q-1] = anticlockwise(gear[q-1])
                    else:
                        gear[q-1] = clockwise(gear[q-1])
                    q -=1
                else:
                    break

        if gear[n] == True:
            q = n-1
            while q <= n:
                if gear[q][2] != gear[q+1][6]:
                    if wise == 1:
                        gear[q+1] = anticlockwise(gear[q+1])
                    else:
                        gear[q+1] = clockwise(gear[q+1])
                    q += 1
                else:
                    break

    for i in range(4):
        print(gear[i])







