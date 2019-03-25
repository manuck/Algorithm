def BubbleSort(data):
    for i in range(len(data)-1, 0, -1): # 4 ~ 1
        for j in range(0,i): # 0 ~ 3
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

data = [2,4,5,3,1]
BubbleSort(data)
print(data)


# call by value : 복사
# call by reference : 원본참조
