import time
def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) +1):
        while n% i == 0:
            factors.append(i)
            n //= i
    if n != 1:
        factors.append(n)
    return factors
start = time.time()
N = int(input())
print(factorize(N))
end = time.time()
print(end - start)

# 210
# [2, 3, 5, 7]
# 2.954352855682373