def gcd(n,m):
    while n % m != 0:
        n,m = m, n%m    
    return m
N,M = map(int,input().split())
print(gcd(N, M))