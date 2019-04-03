import sys
sys.stdin = open("베이비진 게임_input.txt")

'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

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