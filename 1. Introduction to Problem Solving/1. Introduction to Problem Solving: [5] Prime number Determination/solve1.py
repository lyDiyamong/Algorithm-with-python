def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
N = int(input())
import time 
start = time.time()
print("YES" if isPrime(109169) else "NO")
end  = time.time()
print(f'solve elapsed time: {end - start}' )