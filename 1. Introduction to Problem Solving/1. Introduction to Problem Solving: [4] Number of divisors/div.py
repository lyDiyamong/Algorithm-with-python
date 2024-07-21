N = int(input())
import time
start = time.time()
def div(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt
print(div(N))
end = time.time()
print(f'div() elapsed time: {end-start}')