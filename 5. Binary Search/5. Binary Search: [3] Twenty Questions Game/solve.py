def solve(x, s, t):
    low, high = s, t
    while low < high:
        print(low, high, end =' ')
        mid = (low + high)//2
        print(f"Bigger than {mid}", end = " ")
        if x > mid:
            print("Yes")
            low = mid + 1
        else : # if x <= mid
            print('No')
            high = mid
    print(f'Your X is {low}')
    return low 
import random 
S, T = map(int, input().split())
SEED = int(input())
random.seed(SEED)
X = random.randint(S, T)
solve(X, S, T)
# Bigger than 152
# Yes
# Bigger than 201
# No
# Bigger than 177
# Yes
# Bigger than 189
# Yes
# Bigger than 195
# Yes
# Bigger than 198
# Yes
# Bigger than 200
# Yes
# Your X is 201