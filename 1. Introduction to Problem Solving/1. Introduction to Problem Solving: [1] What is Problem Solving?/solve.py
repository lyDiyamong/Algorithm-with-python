def madd(a, b):
    n, m = len(a), len(a[0])
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]
    return c
def mprint(a):
    for i in range(len(a)):
        print(" ".join(map(str, a[i])))
    
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = madd(A, B)
mprint(C)
