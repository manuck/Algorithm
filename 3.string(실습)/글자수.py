import sys
sys.stdin = open("글자수_input.txt")


t = int(input())
for case in range(t):
    a = list(input())
    b = list(input())
    res = 0
    for i in range(len(a)):
        cnt = 0
        for j in range(len(b)):
            if a[i] in b[j]:
                cnt+=1
        if res<cnt:
            res=cnt
    print(f'#{case +1} {res}')