import time

# First code snippet test
def factorize1(n, m):
    fact = []
    while True:
        if m > int(n**0.5):
            fact.append(n)
            break
        elif n % m == 0:
            fact.append(m)
            n //= m
        else: 
            m += 1
    return fact

def solve1(n):
    return factorize1(n, 2)

start1 = time.time()
print(solve1(1000))
end1 = time.time()
print("First code execution time:", end1 - start1)

# Second code snippet test
def factorize2(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n != 1:
        factors.append(n)
    return factors

start2 = time.time()
print(factorize2(1000))
end2 = time.time()
print("Second code execution time:", end2 - start2)
