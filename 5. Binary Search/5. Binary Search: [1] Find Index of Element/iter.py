def binsearch(n, x, S):
    low = 0
    high = n-1
    while low <= high:
        mid = (high+low )//2
        if S[mid] < x:
            low  = mid + 1
        elif S[mid] > x:
            high = mid -1
        else: # s[mid] == x
            return mid
    return -1
def solve(n, m, S, X):
    for i in range(m):
        result = binsearch(n, X[i], S)
        print(result, end = ' ')
    print()
N, M = map(int,input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)