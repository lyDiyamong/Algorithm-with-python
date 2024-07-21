def binsearch(low, high, x, S):
    if low > high:
        return -1
    else:
        mid = (high+low)//2
        if S[mid]== x:
            return mid 
        elif x < S[mid]:
            return binsearch(low, mid - 1, x, S)
        elif x > S[mid]:
            return binsearch(mid+1, high , x, S)
def solve(n, m, S, X):
    for i in range(m):
        result = binsearch(0, n-1, X[i], S)
        print(result, end = ' ')
    print()
N, M = map(int,input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)