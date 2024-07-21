import time
def min_prime_factor(n):
    mpf = [i for i in range(0, n + 1)]
    for i in range(2, int(n ** 0.5)+1):
        if mpf[i] == i:
            for j in range(i*i, n+1, i):
                if mpf[j] == j: 
                    mpf[j] = i
    print(mpf)
    return mpf
def count_factors(n, mpf):
    cnt = 0
    while n != 1:
        cnt += 1
        n //= mpf[n]
    print(cnt)
    return cnt
def solve(n):
    mpf = min_prime_factor(n)
    max_cnt = 0
    for i in range(2, n+1):
        max_cnt = max(max_cnt, count_factors(i, mpf))
    print(max_cnt)
N = int(input())
solve(N)