def myPow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return 1 / myPow(x, -n)
    else:
        if n % 2 == 0:
            half = myPow(x, n/2)
            return half * half
        else:
            half = myPow(x, (n-1)/2)
            return half * half * x
 
        
