import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    start_tick = int(time.time())
    for i in range(100):
        print fib(i)

    print "Total time: %s sec" % (start_tick-(int(time.time())))
