def isprime(n):
    '''Returns True if a given number is prime, otherwise False'''
    factors=[]
    for i in range(2,n):
        if n%i==0:
            factors.append(i)
    if len(factors)>0:
        return False
    else:
        return True


def prime_factors(n)
    '''Returns Prime Factors of a Given Number'''
    n2=n
    prime_factors=[]
    i=2
    while i<n2:
            if n%i==0 and isprime(i):
                n=int(n/i)
                prime_factors.append(i)
                i+=1
            else:
                i+=1
    if n!=1:
        prime_factors.append(n)
    print("Prime Factors: ",prime_factors[:])
            
        
            
