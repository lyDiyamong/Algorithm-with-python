def binsearch(low, high, num, seq):
    if low == high: #base condition
        return -1 if seq[low]% 2 == 1 else low
        # if s[low] % 2 == 1:
        #     return -1 
        # else :
        #     return low
    else:
        mid = (low + high)//2
        if seq[mid]% 2== 0: #even
            return binsearch(low, mid, num, seq)
        else : #odd
            return binsearch(mid+1, high, num, seq)
def solve(num, seq):
    result = binsearch(0, num - 1, num, seq)
    print('There is no even number in the sequence!'if result < 0 else f'The even numbers start from index: {result}')
num = int(input())
seq = list(map(int, input().split()))
solve(num, seq)