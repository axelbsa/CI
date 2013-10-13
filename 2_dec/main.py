def memo(f):
    cache = {}
    def inner_memo(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return inner_memo

@memo
def fib(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-2) + fib(n-1)
    
if __name__ == "__main__":
    print fib(100)
