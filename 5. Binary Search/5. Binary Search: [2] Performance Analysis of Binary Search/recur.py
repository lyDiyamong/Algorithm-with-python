def binsearch(low, high, x, S):
    if low > high:
        return 0
    else:
        mid = (high+low)//2
        if S[mid]== x:
            return 1
        elif x < S[mid]:
            return 1 + binsearch(low, mid - 1, x, S)
        elif x > S[mid]:
            return 1 + binsearch(mid+1, high , x, S)
def solve(n, m, S, X):
    total = 0
    for i in range(m):
        total += binsearch(0, n-1, X[i], S)
    print(total)
N, M = map(int,input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)