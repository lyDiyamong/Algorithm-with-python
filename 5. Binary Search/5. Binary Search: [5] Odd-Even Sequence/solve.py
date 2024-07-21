def binsearch(num, seq):
    low, high = 0, num-1
    while low < high:
        mid = (low + high)//2

        if seq[mid] %2 ==0: ## Narrow down to the left side including mid
            high = mid

        elif seq[mid]%2 == 1: # Narrow down to the right side excluding mid
            low = mid + 1
    if seq[low] % 2 == 0: # Return the index of the first even number
        return low
    else: # No even number found
        return -1
def solve(num, seq):
    result = binsearch(num, seq)
    print('There is no even number in the sequence!'if result < 0 else f'The even numbers start from index: {result}')
num = int(input())
seq = list(map(int, input().split()))
solve(num, seq)
