def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

N,M = map(int,input().split())
print(gcd(N, M))