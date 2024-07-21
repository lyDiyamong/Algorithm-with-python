def solve(String):
    opening = "[{("
    closing = "]})"
    stack = []
    for s in String:
        if s in opening:
            print(f'append {s} to the list')
            stack.append(s)
        elif stack and opening.index(stack[-1]) == closing.index(s):
            #opening index of last value of the stack must have the same index of closing parenthesis
            print(f'Pop it {stack[-1]}')
            stack.pop()
        else :
            return False
    return len(stack) == 0

S = input()
print(solve(S))