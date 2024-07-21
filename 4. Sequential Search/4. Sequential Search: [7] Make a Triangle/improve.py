import time
def solve(n):
    cnt  = 0
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if b <= c and a + b > c:
                # ex : n = 9 , so a = 2, b = 3, c = 4
                # if b <= c : cnt+1
                cnt += 1
    return cnt
start = time.time()
N = int(input())
print(solve(N))
end = time.time()
print(end - start)