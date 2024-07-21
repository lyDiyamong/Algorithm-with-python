from heapq import heappush, heappop

def solve(cmd, heap):
    if cmd[0] == 'push':
        x = int(cmd[1])
        heappush(heap, (abs(x), x))
        # add tuple of index 0 as absolute value and index 1 as original value
    elif cmd[0] == 'pop':
        print(0 if not heap else heappop(heap)[1])
        # print the original value of heap
N = int(input())
heap = []
for _ in range(N):
    cmd = input().split()
    solve(cmd, heap)
# output: it pop only the smallest value, it doesn't care about negative value
# 7
# push -50
# push 10
# pop
# 10
# push -70
# push 30
# pop
# 30
# pop
# -50