
first = '2+3*4/5'
res = []
for i in range(len(first)):
    if first[i] == '+' or first[i] == '-' or first[i]=='*' or first[i]=='/':
        res.append(first[i])
    else:
        print(str(first[i]), end="")

while len(res) != 0:
    print(res.pop(), end="")