'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''

def selectionSort(a):
    f
        for i in range(0, len(a)-1):
            min = 99
            for j in range(i+1, len(a)):
                if a[min] > a[j]:
                    min = j


            a[i], a[min] = a[min], a[i]



arr = [[0 for _ in range(6)] for _ in range()]
for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]