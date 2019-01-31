s = 'Reverse this strings'

def my_strre(a):
    my_str = list(a)
    for i in range(len(my_str)//2):
        t = a[i]
        my_str[i] = my_str[len(my_str)-1-i]
        my_str[len(a)-1-i] = t
    a = ''.join(my_str)
    return a

a = "abcde"
print(my_strre(a))