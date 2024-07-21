def solve(X):
    stack = []
    for x in X:
        if x.isdigit():
            stack.append(int(x))
        else :
            b = stack.pop() # last element
            a = stack.pop()  # before last
            if x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            elif x == '*':
                stack.append(a * b)
            elif x == '/':
                stack.append(a // b)
    print(stack)
    return stack[-1]

X = input()
print(solve(X))


