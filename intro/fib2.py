import time
def fib(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    previous  = 0
    p2p=1
    for index in range(2,n):
        current = previous+p2p
        p2p=previous
        previous = current
    return current
start = time.time()     
print(fib(5))
end = time.time()
print("the time taken : " , end-start)
