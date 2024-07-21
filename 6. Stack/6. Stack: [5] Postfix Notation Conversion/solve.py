# precedence dictionary of operator

pre_op = {
    '(' : 0,
    ')' : 1,
    '+' : 2,
    '-' : 2,
    '*' : 3,
    '/' : 3
}


def solve(Infix):
    stack = []
    postfix = ''
    for i in Infix:
        if i.isalpha():
            postfix+=i
        elif i == '(':
            stack.append(i)
        else: 
            while stack and pre_op[i] <= pre_op[stack[-1]] : # compare the precedence of operator
                postfix+= stack.pop()
            if i == ')': stack.pop() # remove '('
            else : stack.append(i) # operator 
    while stack: # if stack is not empty 
        postfix+= stack.pop() # pop it until there's no more element in the stack
    return postfix

infix = input() 
print(solve(infix))