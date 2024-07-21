# def selection(n, s):
s = [3, 5, 4, 2, 1]
cnt = 0
for i in range(len(s)):
    min_idx = i
    for j in range(i+1, len(s)):
        if s[min_idx] > s[j]:
            min_idx = j
            print(j)
    s[i],s[min_idx] = s[min_idx], s[i] 
    # first iteration : s[i] = 3 swap with s[min_idx] = 1
    cnt+= 1
print(s)
print(cnt)
