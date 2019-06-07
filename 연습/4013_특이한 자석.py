import sys
sys.stdin = open("특이한 자석_input.txt")


t = int(input())

for case in range(1):
    k = int(input())

    gear = []
    for i in range(4):
        gear.append(list(map(int,input().split())))

    # for i in range(4):
    #     print(gear[i])

    for i in range(k):
        gearnum, wise = map(int, input().split())

        if wise == 1:

            for j in range(4):
                if gear[gearnum+j]



