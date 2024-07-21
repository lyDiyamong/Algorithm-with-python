S = [50, 20, 40, 10, 30]
cnt = 0
N = len(S)
for j in range(N):
    for i in range(1, N):
        if S[i-1] > S[i]:
            temp = S[i-1]
            S[i-1] = S[i]
            S[i] = temp
            print(S)
            cnt += 1
            print(i)
    N -= 1 # for less time complexity
print(cnt)






