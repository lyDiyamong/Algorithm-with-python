def binsearch(low, high, num, seq):
    mid = (low +high)//2
    if mid == 0 or mid > num-1:
        return -1
    else :
        if seq[mid-1]<seq[mid]> seq[mid+1]:
            return mid
        elif seq[mid-1] < seq[mid]< seq[mid+1]:
            return binsearch(mid+1, high, num, seq)
        else : #seq[mid-1] > seq[mid]> seq[mid+1]
            return binsearch(low, mid-1, num, seq)
num = int(input())
seq = list(map(int, input().split()))
def solve(num, seq):
    result = binsearch(0, num-1, num, seq)
    print(result, seq[result])
solve(num, seq)