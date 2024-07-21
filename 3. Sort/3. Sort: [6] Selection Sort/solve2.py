def selection(n, s):
    cnt = 0
    for i in range(n-1):
        min_v, min_idx = s[i], i
        for j in range(i+1, n):
            if s[j] < min_v:
                min_v, min_idx = s[j], j
        if i != min_idx:
            s[i], s[min_idx] = s[min_idx], s[i]
            cnt += 1
            print(s)
    return cnt
N = int(input())
S = list(map(int, input().split()))
print(selection(N, S))
