def palindrome(palin):
    num = 0
    reverse = 0
    origin = palin # for storing the source number
    while palin != 0:
        num = palin % 10
        palin //= 10
        reverse = num + (reverse*10)
    if reverse == origin:       
        return True
    return False

N = [123432, 33, 372, 901, 232]
def palindromeS(n):
    strN = list(map(str, n))
    cnt = 0
    for i in strN:        
        rev = i[::-1]
        if rev == i:
            cnt += 1
    return cnt
print(palindromeS(N))