s = [5, 3, 4, 1, 2]
n = len(s)
cnt = 0
for i in range(1, n):
    for j in range(i-1, -1,-1):
        if s[i] < s[j]:
            s[i], s[j] = s[j+1], s[i]
print(s)