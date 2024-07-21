def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
import time
N = int(input())
start = time.time()

print(fact(N))
end = time.time()
print(f'{end-start}')