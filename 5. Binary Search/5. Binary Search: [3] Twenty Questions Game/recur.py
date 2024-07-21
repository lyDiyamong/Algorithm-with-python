def solve(target, start, end):
    if start >= end :
        print(f'Your Target is {start}')
        return start
    else :
        mid  = (start + end)//2
        print(f"Bigger than {mid}?")
        if target > mid:
            print('Yes')
            return solve(target, mid+1, end)
        else:
            print("No")
            return solve(target, start, mid)
import random 
S, T = map(int, input().split())
SEED = int(input())
random.seed(SEED)
X = random.randint(S, T)
solve(X, S, T)