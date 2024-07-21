def cut(num, seq, height):
    length = 0
    for i in range(num):
        if seq[i] > height:
            length += (seq[i] - height ) if seq[i] > height else 0
    return length
def binsearch(low, high, num, wood, seq):
    print(low, high)
    if low >= high :
        return low - 1
    else:
        mid = (low + high)//2
        if cut(num, seq, mid) < wood:
            return binsearch(low, mid, num, wood, seq)
        else :
            return binsearch(mid+1, high, num, wood, seq)
def solve(num, wood, seq):
    result = binsearch(0, max(seq), num, wood, seq)
    return result
Num, wood = map(int, input().split())
Seq = list(map(int, input().split()))
print(solve(Num, wood, Seq))