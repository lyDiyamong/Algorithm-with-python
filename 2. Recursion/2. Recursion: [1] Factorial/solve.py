def fact(n):
    if n <= 0:
        return 1
    
    return n * fact(n-1)
import sys
import time
sys.setrecursionlimit(10**5)
N = int(input())
start = time.time()

print(fact(N))
end = time.time()
print(f'{end-start}')