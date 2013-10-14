import time,sys
sys.setrecursionlimit(100000)

try: import numpy; f_n = True
except: f_n = False

n = 1200
f_n = False

def memo(f):
    cache = {}
    def inner_memo(n):
        if n in cache:
            print cache[n]
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
    
def fib_numpy(n,vector):
    vector[0] = vector[1] = 1
    for index in range(2,n):
        print >> sys.stderr, index
        vector[index] = vector[index-1] + vector[index-2]
    return vector[n-1]

if __name__ == "__main__":

    start_tick = time.time()
    if f_n:
        vector = numpy.zeros(n)
        fib_numpy(n, vector)
        print vector[len(vector)-1]
    else:
        fib(n)
        
    print "-----------------------------------------------------"
    print "\r\r Total time: %s sec" % (time.time() - start_tick)
