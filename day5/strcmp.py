def strcmp(str1, str2):
    i = 0
    if len(str1) != len(str2):
        return False
    else:
        while i < len(str1) and i < len(str2): # and i < len(str2) 없어도 동작
            if str1[i] != str2[i]:
                return  False
            i += 1
    return True

a = "abcde"
b = "abcde"

print(strcmp(a, b))
print(a == b)