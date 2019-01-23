'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''




n, m = map(int, input().split())
mylist = [[0 for _ in range(m)] for _ in range(n)]  # _ : 이름없는 변수
print()
print(mylist) # 리스트가 0으로 초기화가 되어있는지 확인
for i in range(n):
    mylist[i] = list(map(int, input().split()))
print(mylist)