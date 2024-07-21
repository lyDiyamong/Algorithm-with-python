def cut(num, seq, height):
    length = 0
    for i in range(num):
        if seq[i] > height:
            length += (seq[i] - height ) if seq[i] > height else 0
    return length
def binsearch(num, wood, seq):
    low = 0
    high = max(seq)
    while low < high:
        print(low, high)
        mid = (low + high)//2
        if cut(num, seq, mid) < wood:
            high = mid #(right half)
        else: 
            low = mid + 1 #(left half)
    return low -1
def solve(num, wood, seq):
    result = binsearch(num, wood, seq)
    return result
Num, wood = map(int, input().split())
Seq = list(map(int, input().split()))
print(solve(Num, wood, Seq))