N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]
print(P)

def sort(n, p):
    p.sort(key = lambda x : (x[0],-x[1]))
    for i in range(len(p)):
        print(' '.join(map(str, p[i])))
        
sort(N, P)