def solve(s, x):
    for i in range(n):
        for j in range(n):
            if x[j] == s[i]:
                print(i)
            else:
                print(-1)
n = 4
s = [1,2,3,4]
x = [3, 4, 5, 1]
solve(s,x)
