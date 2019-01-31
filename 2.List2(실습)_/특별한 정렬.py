import sys
sys.stdin = open("특별한 정렬_input.txt")

def selsort(a):
    for i in range(0, len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if i % 2 == 1:
                if a[min] > a[j]:
                    min = j
            if i % 2 == 0:
                if a[min] < a[j]:
                    min = j
        a[i], a[min] = a[min], a[i]
    return a[0:10]

t = int(input())
for i in range(int(t)):
    n = input()
    a = list(map(int, input().split()))
    result = ''
    for j in range(len(selsort(a))):
        result += str(selsort(a)[j])+' '
    print(f'#{i+1} {result}')


# def selsort(a):
#     for i in range(0, len(a) - 1):
#         min = i
#         for j in range(i + 1, len(a)):
#             if a[min] > a[j]:
#                 min = j
#         a[i], a[min] = a[min], a[i]
#
# t = int(input())
#
# for i in range(int(t)):
#     n = input()
#     a = list(map(int, input().split()))
#
#     li = []
#
#     selsort(a)
#
#     if int(n) % 2 == 0:
#         for j in range(int(int(n)/2)):
#             li.append(a[~j])
#             li.append(a[j])
#     else:
#         for j in range(int((int(n)+1)/2)):
#             li.append(a[~j])
#             li.append(a[j])
#         del li[~0]
#     result = ''
#     for j in range(10):
#         result += str(li[j]) + ' '
#     if result[~0]==' ':
#         result = result[0:~0]
#     print(f'#{i+1} {result}')