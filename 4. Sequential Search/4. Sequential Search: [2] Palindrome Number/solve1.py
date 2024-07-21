def palindrome(n):
    reverse = 0
    m = n
    while m > 0:
        reverse *= 10 
        reverse = reverse + (m%10)
        m //= 10
    if n == reverse:
        return True
    return False
def solve(f, l):
    cnt = 0
    for i in range(f, l+1):
        if palindrome(i):
            cnt += 1
    return cnt
F, L = map(int, input().split())
print(solve(F, L))
    
    