def solve(n, s):
    even = []
    odd = []
    for i in s:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort(reverse= True)
    odd.sort()
    print(*odd)
    print(*even)
N = int(input())
S = list(map(int, input().split()))
solve(N, S)