import sys
sys.stdin = open("염라대왕의 이름정렬_input.txt")

t = int(input())
for case in range(1):
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(str(input()))

    print(name_list)
    for i in range(n):
        print(len(name_list[i]))

    for i in range(n):
        k = len(name_list[i])
        for j in range(len(k)):
