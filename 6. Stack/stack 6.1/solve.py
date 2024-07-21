def solve(cmd, stack):
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print('Oops')
        else:
            print(stack.pop())

    elif cmd[0] == 'peek':
        print(stack[-1])

    elif cmd[0] == 'size':
        print(len(stack))

    elif cmd[0] == 'empty':
        print(len(stack)==0)
N = int(input())
stack = []
for _ in range(N):
    cmd = list(map(str, input().split()))
    solve(cmd, stack)