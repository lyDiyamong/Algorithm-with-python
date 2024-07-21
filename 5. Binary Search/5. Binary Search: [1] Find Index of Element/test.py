def solve(s, x):
    low = 0
    high = len(s)-1
    mid = 0
    while low <= high:
        mid = (high+low )//2
        if s[low] > s[high]:
            return -1
        else:
            if s[mid] < x:
                low  = mid + 1
            elif s[mid] > x:
                high = mid -1
            else: # s[mid] == x
                return mid
x = 10
s = [2, 3, 4, 5, 6, 7]
print(solve(s, x))