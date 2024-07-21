def median(n, s): # Remove the middle number after sorted one by one
    s.sort()
    while len(s) > 0:
        mid = (len(s)-1)//2
        print(s[mid],end=' ')
        s.remove(s[mid])
N = int(input())
S = list(map(int,input().split()))

median(N, S)