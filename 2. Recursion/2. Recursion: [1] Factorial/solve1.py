def fact(n):
    fact = 1
    while n != 0:
        fact*= n
        n -= 1
    return fact
import time
N = int(input())
start = time.time()

print(fact(N))
end = time.time()
print(f'{end-start}')