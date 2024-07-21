import time
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
def is_palin(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)

def find_prpa(n, m):
    cnt = 0
    for i in range(n, m+1): 
        if is_prime(i) and is_palin(i):
            print(i)
            cnt += 1
    return cnt 
N, M = map(int, input().split())
start = time.time()
print(find_prpa(N, M))
end = time.time()
print(f'solve() elapsed time: {end - start}')