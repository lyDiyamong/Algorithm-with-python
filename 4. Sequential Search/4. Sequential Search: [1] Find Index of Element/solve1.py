def seqSearch(n, s, x):
    for i in range(n):
        if x == s[i]:
            return i
    return -1
def solve(n, m, s, x):
    for i in range(m):
        print(seqSearch(n, s, x[i]), end = ' ')
    print()
# n = m = 4
# s = [1,2,3,4]
# x = [3, 4, 5, 1]
N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)