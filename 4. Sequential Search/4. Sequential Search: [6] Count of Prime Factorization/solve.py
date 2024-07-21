import time
def cnt_factor(n):
    cnt = 0
    for i in range(2, int(n**0.5) +1):
        while n% i == 0:
            cnt+= 1
            n //= i
    if n != 1:
        cnt += 1
    return cnt

def solve(n):
    max_cnt = 0
    for i in range(2, n+1):
        max_cnt = max(max_cnt, cnt_factor(i))
        print(f"Number {i}, factor:{cnt_factor(i)}")
    print(max_cnt)
start = time.time()
N = int(input())
solve(N)
end = time.time()
print(end - start)

# output:
# 10
# Number 2, factor:1
# Number 3, factor:1
# Number 4, factor:2
# Number 5, factor:1
# Number 6, factor:2
# Number 7, factor:1
# Number 8, factor:3
# Number 9, factor:2
# Number 10, factor:2
# 3
# 1.7115750312805176