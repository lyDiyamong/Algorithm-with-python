def div(n):
    sqrtn = int(n ** 0.5) # square root of n
    # use int func cuz range can't take float as argument
    
    cnt = 0
    for i in range(1, sqrtn + 1): # make the for loop to run only from 1 to 
                                        #square root of n times
        if n % i == 0:
            cnt += 2
    if sqrtn ** 2 == n: # condition for perfect square number
        cnt -= 1
    return cnt
N = int(input())
import time 
start = time.time()
print(div(N))
end = time.time()
print(f'div() elasped time: {end - start}')