# {1, 2, 3}

def babyGin(data):
    for i1 in range(len(data)):
        for i2 in range(len(data)):
            if i2 != i1:
                for i3 in range(len(data)):
                    if i3 != i1 and i3 != i2:
                        for i4 in range(len(data)):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                for i5 in range(len(data)):
                                    if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        for i6 in range(len(data)):
                                            if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                  # print(data[i1], data[i2], data[i3], data[i4], data[i5], data[i6])
                                                  check = 0
                                                  if data[i1] == data[i2] and data[i2] == data[i3]:
                                                      check += 1
                                                  if data[i4] == data[i5] and data[i5] == data[i6]:
                                                      check += 1
                                                  if data[i1] + 1 == data[i2] and data[i2] + 1 == data[i3]:
                                                      check += 1
                                                  if data[i4] + 1 == data[i5] and data[i5] + 1 == data[i6]:
                                                      check += 1
                                                  if check == 2:
                                                      return True
    return  False
# data = [0,5,4,0,6,0]
data = [0,1,0,1,2,3]
if babyGin(data):
    print("Baby Gin")
else:
    print("Not")