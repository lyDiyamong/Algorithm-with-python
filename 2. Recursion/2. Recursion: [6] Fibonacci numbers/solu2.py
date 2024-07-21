def fibo(n):
    if 0 < n <= 2:
        return 1
    else:
        a = b = 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b
N = int(input())
print(fibo(N))
# e.g n = 4
# f: 1, 1 = 1 , 1 + 1   b = 2
# s : 1, 2 = 1, 1 + 2   b = 3
# t : 2, 3, = 3, 2 + 3