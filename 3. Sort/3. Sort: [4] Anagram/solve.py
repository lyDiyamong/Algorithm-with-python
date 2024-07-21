def anagram(n, s):
    for i in range(1,len(s)):
        if sorted(s[i-1]) == sorted(s[i]):
            print(''.join(s[i-1]))
            s.remove(s[i])
        else:
            print(''.join(s[i-1]))
N = int(input()) 
S = list(map(str, input().split()))
anagram(N, S)