def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]


a = [19, 12, 8, 4, 23, 17]
selectionSort(a)
print(a)
