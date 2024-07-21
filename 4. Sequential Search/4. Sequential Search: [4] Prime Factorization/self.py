import time
def factorize(n, m):
    fact = []
    while True:
        if m > int(n**0.5):
            print(n,'this is n')
            fact.append(n)
            break
        elif n % m == 0:
            fact.append(m)
            print(m)
            n //= m
        else: 
            m += 1
    return fact
def solve(n):
    factors = factorize(n, 2)
    print(factors)

start = time.time()
N = int(input())
solve(N)
end = time.time()
print(end - start)