def find_prime(n):
    sieve = [0,0]+[1]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == 1:
            for j in range(i*i, n+1, i):
                sieve[j] = 0
    return [i for i in range(n+1) if sieve[i] == 1]
def binsearch(low, high, target, seq):
    if low > high:
        return -1
    else:
        mid =(low +high)//2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            return binsearch(low, mid-1, target, seq)
        else:
            return binsearch(mid+1, high, target, seq)
def solve(num, seq, max_num):
    primes = find_prime(max_num)
    for i in range(num):
        result = binsearch(0, len(primes)-1 ,seq[i], primes)
        print(result + 1, end = " ")
    print()
N = int(input())
S = list(map(int, input().split()))
solve(N, S, 100000)   