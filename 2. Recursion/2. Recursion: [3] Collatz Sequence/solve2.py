def collatz(n):
    lst = []
    while n > 1:
        if n % 2 == 0:
            lst.append(n // 2)
            n //= 2
        else:
            lst.append(n * 3 + 1)
            n = 3*n + 1
    return lst
result = collatz(10000000000000000000000000000000000000000000000000000000000000000)
print(len(result))
print(*result)