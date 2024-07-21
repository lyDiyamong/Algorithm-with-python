def factor(n):
    if n < 2:
        return []
    else :
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                print(i)
                return [i] + factor(n//i)
        return [n]
print(*factor(16))
# 2
# 2
# 2
# 2 2 2 2