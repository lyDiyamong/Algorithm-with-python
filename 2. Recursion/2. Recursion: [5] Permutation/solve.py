N = int(input())
S = [chr(ord('A')+ i)  for i in range(N)]

def permute(i,n,s):
    if i == n - 1:
        print(*s)
    else:
        for j in range(i,n):
            s[i], s[j] = s[j], s[i] # find the combination
            permute(i+1, n, s)
            s[i], s[j] = s[j], s[i] # backtrack to the original string in list
            
permute(0, N, S)
