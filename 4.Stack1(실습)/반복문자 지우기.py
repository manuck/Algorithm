import sys
sys.stdin = open("반복문자 지우기_input.txt")

T = int(input())
for case in range(1, T+1):
    data = input()
    s = []
    for i in range(len(data)):
        if len(s)==0:
            s.append(data[i])
        else:
            if s[-1] == data[i]:
                s.pop()
            else:
                s.append(data[i])
    print(f'#{case} {len(s)}')