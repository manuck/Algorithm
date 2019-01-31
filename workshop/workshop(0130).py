import sys
sys.stdin = open("0130_input.txt")

t = int(input())
for case in range(t):
    a = input()
    data = list(map(str, input().split()))
    li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = []
    for i in range(len(li)):
        for j in range(len(data)):
            if data[j] == li[i]:
                result.append(li[i])
    result = ' '.join(result)
    print(f'#{case+1}')
    print(result)