import time

try: import numpy;found_numpy = True
except: found_numpy = False

n = 1200

def fib_numpy(n,vector):
    vector[0] = vector[1] = 1
    for index in range(2,n):
        print index
        vector[index] = vector[index-1] + vector[index-2]
    return vector[n-1]

if __name__ == "__main__":

    if found_numpy:
        start_tick = time.time()
        vector = numpy.zeros(n)
        fib_numpy(n, vector)
        print vector[len(vector)-1]
        print "-----------------------------------------------------"
        print "\r\r Total time: %s sec" % (time.time() - start_tick)
    else:
        # Do it some other way
        pass

