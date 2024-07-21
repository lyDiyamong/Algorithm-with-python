def solve(n, seq):
    stack = []
    operation = ""
    j = 0
    for i in range(1, n + 1):
        stack.append(i)
        operation += '+'
        while stack and seq[j] == stack[-1]: 
            # check if list is not empty & last elemnt of seq equal to stack[-1]
            stack.pop()
            operation += '-'
            j += 1
            # increase index of seq
    return 'No' if stack else operation
N = int(input('Number : '))
Seq = list(map(int, input('Sequence input:').split(' ')))

print(solve(N, Seq))