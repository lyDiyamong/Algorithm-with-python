def solve(N , M):
    return (M - N + 1)*(N + M)//2
N, M = map(int, input().split())
print(solve(N, M))