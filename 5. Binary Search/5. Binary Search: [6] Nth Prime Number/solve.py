def find_prime(n):
    sieve = [0,0]+[1]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == 1:
            for j in range(i*i, n+1, i):
                sieve[j] = 0
    return [i for i in range(n+1) if sieve[i] == 1]
    # Create a list of prime nums by gathering the indices with a value of 1 in the sieve list 
# def store_prime(n):
#     prime_lst = []
#     sieve = find_prime(n)
#     for i in range(2, n+1):
#         if sieve[i] == 1:
#             prime_lst.append(i)
#     return prime_lst
def binsearch (target, num, seq):
    low, high = 0, num-1
    while low <= high:
        mid = (low+high)//2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            high = mid - 1
        else: #target>seq[mid]
            low = mid + 1
    return -1
def solve(num, seq, max_num):
    primes = find_prime(max_num)
    for i in range(num):
        result = binsearch(seq[i], len(primes), primes)
        print(result + 1, end = " ")
    print()
N = int(input())
S = list(map(int, input().split()))
solve(N, S, 100000)     
