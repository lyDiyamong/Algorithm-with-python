def binsearch(n, x, S):
    cnt = 0
    low = 0
    high = n-1
    while low <= high:
        cnt += 1
        mid = (high+low )//2
        if S[mid] < x:
            low  = mid + 1
        elif S[mid] > x:
            high = mid -1
        else: # s[mid] == x
            return cnt
    return cnt
def solve(n, m, S, X):
    total = 0
    for i in range(m):
        total += binsearch(n, X[i], S)
    print(total)
N, M = map(int,input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)