def solve(target, start, end):
    low, high = start, end
    while low < high:
        mid = (low + high) // 2
        print(f"Bigger than {mid}?")
        if target > mid:
            print("Yes")
            low = mid + 1
        else:  # if target <= mid
            print("No")
            high = mid 
    print(f'Your target is {low}')
    return low 

# Example usage:
target = 50
start = 0
end = 100
solve(target, start, end)
