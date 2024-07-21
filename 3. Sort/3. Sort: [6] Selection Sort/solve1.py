def solve(n, s):
    cnt = 0
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if s[min_idx] > s[j]:
                min_idx = j
                # print(j)
        s[i],s[min_idx] = s[min_idx], s[i] 
        cnt+= 1
        print(s)
    return cnt
N = int(input())
S = list(map(int, input().split()))
print(solve(N, S))
