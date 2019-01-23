import sys
sys.stdin = open("card_input.txt")
t = input()
for i in range(int(t)):
    n = input()
    a = input()
    c = [0] * 10
    for j in range(len(a)):
        c[int(a[j])] += 1
    maxindex = 0
    maxvalue = c[0]
    for j in range(10):
        if maxvalue <= c[j]:
            maxvalue = c[j]
            maxindex = j
    print(f'#{i+1} {maxindex} {maxvalue}')