def isPrime(n):
    cnt = 0
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    
    if cnt > 0 or n == 1:
        return 'Not Prime'
    return 'Prime'
N = 636326
print(isPrime(N))