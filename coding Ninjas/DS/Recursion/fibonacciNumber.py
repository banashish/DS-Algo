from sys import setrecursionlimit
setrecursionlimit(11000)

n = 7

def fibonacci(n):
    if(n == 0 or n == 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))