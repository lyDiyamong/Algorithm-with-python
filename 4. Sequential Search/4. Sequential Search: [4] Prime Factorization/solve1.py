import time
def factorize(n, m):
    if n < 2: # exit condition
        return []
    elif m > int(n**0.5): #exit condition
        return [n]
    elif n % m == 0:
        print(n, m)
        return [m] + factorize(n//m, m)
    else :
        print(n,m)
        return factorize(n, m+1)
def solve(n):
    factors = factorize(n, 2)
    print(factors)

start = time.time()
N = int(input())
solve(N)
end = time.time()
print(end - start)
# Output
# 210
# 210 2
# 105 2
# 105 3
# 35 3
# 35 4
# 35 5
# [2, 3, 5, 7]
# 2.0955381393432617