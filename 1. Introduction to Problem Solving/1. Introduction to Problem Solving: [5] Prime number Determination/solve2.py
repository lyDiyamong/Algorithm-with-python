def isPrime(n):
    sqrtn = int(n ** 0.5)
    if n <= 1:
        return False
    for i in range(2, sqrtn+1): # sqrt + 1 cuz we need to check the number of perfect square
        # and protection of small number 
        if n % i == 0:
            return False
    return True
N = int(input())
print("YES" if isPrime(N) else "NO")