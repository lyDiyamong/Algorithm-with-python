class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        return self.queue.append(x)
    def dequeue(self):
        return 'Oops' if self.empty() else self.queue.pop(0)
    def peek(self):
        return None if self.empty() else self.queue[0]
    def size(self):
        return len(self.queue)
    def empty(self):
        return self.size() == 0

queue = Queue()
n = int(input('Enter number of command'))
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'enqueue':
        queue.enqueue(cmd[1])
    elif cmd[0] == 'dequeue':
        print(queue.dequeue())
    elif cmd[0] == 'peek':
        print(queue.peek())
    elif cmd[0] == 'size':
        print(queue.size())
    elif cmd[0] == 'empty':
        print(queue.empty())

    