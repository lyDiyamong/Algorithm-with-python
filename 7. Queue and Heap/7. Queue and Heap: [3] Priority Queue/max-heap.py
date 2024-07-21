from heapq import heappush, heappop

def solve(cmd, heap):
    if cmd[0] == 'push':
        heappush(heap, -int(cmd[1]))
        # the biggest value is also the smallest value in the heap if 
        # u put - operator
    elif cmd[0] == 'pop':
        print(0 if not heap else -heappop(heap))
        # we pop the smallest value but put back the - operator
N = int(input())
heap = []
for _ in range(N):
    cmd = input().split()
    solve(cmd, heap)

# output
# 8 
# push 40
# push 44
# push 10
# push -20
# pop
# 44
# pop
# 40
# pop
# 10
# pop
# -20