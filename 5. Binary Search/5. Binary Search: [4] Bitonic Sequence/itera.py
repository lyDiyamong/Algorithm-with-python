def binsearch(num, seq):
    low, high= 0, num -1
    mid = (low + high)//2
    while mid != 0 and mid !=  num-1:
        mid = (low + high)//2
        if seq[mid-1]< seq[mid] > seq[mid+1]:
            return mid
        elif seq[mid-1] < seq[mid] < seq[mid+1]:
            low = mid +1
        else :
            high = mid - 1
    return -1

num = 7
seq = [22, 33 ,55, 32, 23, 11, 9]
result = binsearch(num, seq)
print(result, seq[result])