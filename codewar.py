def acum(s):
    lst = []
    for i in range(len(s)):
        lst.append(s[i].upper() + s[i] * (i))
    return lst
print(acum('Absjuf'))