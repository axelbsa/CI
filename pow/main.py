# Inserting random comment, needd"#¤"#¤ a little more comment 

f = lambda n,x: 1 if x==0 else (n*f(n,x-1) if x>0 else 1.0/(n*f(n,abs(x)-1.0)))

def pow(num, power):
    sum_q = 1.0
    if power < 0:
        sum_q = pow(1.0/num, -1.0 * power)
        return sum_q
    elif power == 0:
        return 1
    for i in range(int(power)):
        sum_q *= num
    return sum_q

def rec(n,x):
    if x == 0: 
        return 1
    if x < 0:
        return 1.0/(n*rec(n,(-1*x)-1.0))
    if x > 0:                           
        return n*rec(n,x-1)

if __name__ == "__main__":
    print pow(2.0,8.0)
    print rec(2.0, -3.0)
    print f(2.0, -3,0)
