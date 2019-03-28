import sys
sys.stdin = open("베이비진 게임_input.txt")


t = int(input())
for case in range(1, t+1):
    a = list(map(int, input().split()))

    # print(a)
    player1 = []
    player2 = []
    flag = 0
    for i in range(len(a)):
        if flag != 0:
            break

        if i % 2 == 0:
            player1.append(a[i])
            if len(player1) >= 3:
                player1.sort()
                # print(player1)
                for i in range(len(player1)-2):
                    if player1[i] == player1[i+1]:
                        if player1[i+1]+1 == player1[i+2] and player1[i+1]-1 == player1[i-1]:
                            flag = 1
                            break
                    if player1[i] == player1[i+1] and player1[i+1] == player1[i+2]:
                        flag = 1
                        break
                    if player1[i]+1 == player1[i+1] and player1[i+1]+1 == player1[i+2]:
                        flag = 1
                        break

        else:
            player2.append(a[i])
            if len(player2) >= 3:
                player2.sort()
                # print(player2)
                for i in range(len(player2)-2):
                    if player2[i] == player2[i+1]:
                        if player2[i+1]+1 == player2[i+2] and player2[i+1]-1 == player2[i-1]:
                            flag = 2
                            break
                    if player2[i] == player2[i+1] and player2[i+1] == player2[i+2]:
                        flag = 2
                        break
                    if player2[i]+1 == player2[i+1] and player2[i+1]+1 == player2[i+2]:
                        flag = 2
                        break

    print('#%i ' % (case),end = "")
    if flag == 1:
        print(1)
    elif flag == 2:
        print(2)
    else:
        print(0)