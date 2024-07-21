class Stack:
    def __init__(self):
        self.stack = []
    def push(self, X):
        self.stack.append(X)
    def pop(self):
        return None if self.empty() else self.stack.pop()
    def peek(self):
        return None if self.empty() else self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return len(self.stack) == 0

def solve(string):
    open_brackets = "[{("
    close_brackets = "]})"
    stack = Stack()
    for s in string:
        if s in open_brackets:
            stack.push(s)
            print('Append', s, 'into the stack:', stack.stack)
        elif s in close_brackets:
            if not stack.empty() and open_brackets.index(stack.peek()) == close_brackets.index(s):
                print('Pop', stack.peek(), 'from the stack')
                stack.pop()
                print('Current stack:', stack.stack)
            else:
                return False
    return stack.empty()

String = input("Enter a string of brackets: ")
print('Yes' if solve(String) else 'No')
