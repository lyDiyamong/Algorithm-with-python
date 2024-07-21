
from stack_class import Stack
def visible(num, seq):
    stick = Stack()
    for i in range(num):
        print(f'Push {seq[i]} into the stack')
        while not stick.empty() and seq[i] >= stick.peek():
            print(f'Pop {stick.display()} out of the stack')
            stick.pop()

        stick.push(seq[i])
    print(stick.stack)
    return stick.size()
Num = int(input())
Seq = list(map(int, input().split()))
print(visible(Num, Seq))