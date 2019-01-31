def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]
        if  c >= '0' and c <= '9':  # 문자열도 크고 작음을 비교 가능
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit # 여기가 핵심 # 십진수라 10 곱함 # 2진수면 2를 곱한다.
        i += 1
    return value

a = "123"
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))