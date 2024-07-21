def fibo(n):
    if 0< n <= 2:
        return 1
    else : 
        return fibo(n - 1) + fibo(n - 2)
# N = int(input())
# print(fibo(N))
for i in range(1, 15):
    print(fibo(i))