########################################################
# Naive recursive fibonacci implentation.
# Were n = 4 it will compute the following tree
#
#                       fib(4)
#
#             fib(3)             fib(2)
#
#         fib(2)   fib(1)     fib(1)   fib(0)
#
#      fib(1)  fib(0) 
#
# This gives roughly a time complexsity of O(2^n) 
# given that for each call to fib, two new calls 
# are being done. 
#######################################################

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print fib(10)
