import time
def find_primes(n):
    sieve =[0,0] + [1] * (n-1) # [0, 0] means we initially cut out 0, 1 
    for i in range(2, n+1):
        if sieve[i] == 1:
            for j in range(i+i, n + 1, i):
                sieve[j] = 0
    return sieve
def solve(n):
    sieve = find_primes(n)
    return sum(sieve)
start = time.time()
N = int(input())
print(solve(N))
end = time.time()
print(end - start)

# eg. n = 10
#  [0, 0 , 1, 1, 1, 1, 1, 1, 1, 1, 1]
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# if sieve[i] = 0
# 1st  for j in range(2 + 2, 11, 2) 
#           sieve[j] = 0 we tackle it (means we cut it out as it's not a prime anymore)
# 2nd for j in range(3+3, 11, 3)
#           sieve[j] = 0 we tackle it (means we cut it out as it's not a prime anymore)
# 3rd for j in range(5+5, 11, 5)
#           sieve[j] = 0  we tackle it (means we cut it out as it's not a prime anymore)
